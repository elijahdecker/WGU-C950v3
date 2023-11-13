# Student ID: 010229142
import datetime

from HashTable import HashTable
from Package import Package
from Truck import Truck
import csv

package_hash = HashTable()
package_ids = []

# Read the data from packages.csv
with open('packages.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    packages = list(reader)

# Read the data from distances.csv
with open('distances.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    distances = list(reader)

# Use the data from the packages.csv file to populate a hash table
def populate_package_hash():
    for row in packages:
        # If the package has the wrong address listed and has the ID of 9, update the address
        if (row[7] == "Wrong address listed" and row[0] == "9"):
            p = Package(row[0], "410 S State St", "Salt Lake City", "UT", "84111", row[5], row[6], row[7], "At the hub")
            package_ids.append(int(p.id))
            package_hash.insert(int(p.id), p)
        else:
            p = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], "At the hub")
            package_ids.append(int(p.id))
            package_hash.insert(int(p.id), p)

# Find the index of an address in the distances.csv file
def find_address(address):
    i = 0
    for col in distances[0]:
        if address in col:
            return i
        i = i + 1

# Nearest neighbor algorithm
def calculate_route(truck, end_time):
    undelivered_packages = truck.packages.copy()
    # Do not run if the truck will not have departed
    if (end_time >= truck.current_time):

        # Change the status of each package on the truck to "En route"
        for package_id in truck.packages:
            package = package_hash.search(package_id)
            package.status = "En Route by " + truck.name

        while len(undelivered_packages) > 0:
            least_distance = 1000.0
            next_package = None

            # Iterate through all undelivered packages to find the
            # next delivery address nearest to the truck's nearest location
            for package_id in undelivered_packages:

                # Find the indexes for the current address of the truck and the address
                # of the next package
                curr_loc = int(find_address(truck.current_location))
                package = package_hash.search(package_id)
                next_loc = int(find_address(package.address))

                # The order of the location indexes to get the distance depends on which index is greater
                if (next_loc > curr_loc):
                    distance = float(distances[next_loc][curr_loc])
                else:
                    distance = float(distances[curr_loc][next_loc])

                # If the distance between the two addresses is less than the least distance found,
                # set the new least distance and next package
                if (distance < least_distance):
                    next_package = package
                    least_distance = distance

            # Mark a package as "delivered" by removing it from the undelivered packages list
            undelivered_packages.remove(int(next_package.id))

            # Update what the time is by estimating the time it takes to deliver the next package
            truck.current_time = truck.current_time + datetime.timedelta(hours=(least_distance / truck.speed))

            # If the current time has gone past the end time set, set the current time and break the loop
            if (truck.current_time > end_time):
                truck.current_time = end_time
                break;

            # Mark the package as delivered
            next_package.status = "Delivered @ " + str(truck.current_time) + " by " + truck.name

            # Update the package in the hash table
            package_hash.insert(int(next_package.id), next_package)

            # Update the current location of the truck
            truck.current_location = next_package.address

            # Add to the distance traveled by the truck
            truck.distance += least_distance
    return truck

# Main program
if __name__ == '__main__':


    while True:
        # Populate hash table from package CSV file
        package_ids = []
        populate_package_hash()

        # Create truck objects and manually load packages
        truck1_packages = [1, 13, 14, 15, 16, 19, 20, 23, 29, 30, 31, 34, 37, 40]
        truck1 = Truck("Truck 1", 18, datetime.timedelta(hours=8), truck1_packages, "4001 South 700 East")
        truck2_packages = [2, 3, 4, 5, 6, 10, 18, 21, 22, 26, 35, 36, 38]
        truck2 = Truck("Truck 2", 18, datetime.timedelta(hours=9, minutes=15), truck2_packages, "4001 South 700 East")
        truck3_packages = [7, 8, 9, 11, 12, 17, 24, 25, 27, 28, 32, 33, 39]
        truck3 = Truck("Truck 3", 18, datetime.timedelta(hours=10, minutes=30), truck3_packages, "4001 South 700 East")

        # Menu
        print("\n=============================================================================\n" +
              "p: Show all package information and total mileage\n" +
              "s {package_id} {time (ex: 13:10)}: Show single package information with time\n" +
              "a {time (ex 13:10)}: Show all packages with time\n" +
              "q: Exit program\n" +
              "=============================================================================")
        command = input("\ncommand: ").split(" ")

        if command[0] == "p":

            # Set the end time to "EOD" (11pm)
            time = datetime.timedelta(hours=23)

            # Find what the statuses are of all the packages by EOD
            truck1 = calculate_route(truck1, time)

            truck2 = calculate_route(truck2, time)

            truck3 = calculate_route(truck3, time)

            # Print package info
            print("Package ID, Address, City, State, Zip, Delivery Deadline, Weight (kg), Notes, Status")
            for id in package_ids:
                package = package_hash.search(id)
                print(package)
            print("Distance traveled: " + str(round(truck1.distance + truck2.distance + truck3.distance, 2)))

        elif command[0] == "s":
            # Short circuit if not all command parameters are given
            if (len(command) < 3):
                print("Please provide both parameters")
                continue

            # Parse the package id and end time from the input
            package_id = int(command[1])
            time_param = command[2].split(":")
            time = datetime.timedelta(hours=int(time_param[0]), minutes=int(time_param[1]))

            # Find what the statuses are of all the packages by the given time
            truck1 = calculate_route(truck1, time)

            truck2 = calculate_route(truck2, time)

            truck3 = calculate_route(truck3, time)

            # Print package info
            print("Package ID, Address, City, State, Zip, Delivery Deadline, Weight (kg), Notes, Status")
            package = package_hash.search(package_id)
            print(package)

        elif command[0] == "a":
            # Short circuit if not all command parameters are given
            if (len(command) < 2):
                print("Please provide a time")
                continue

            # Parse the time parameter from the input
            time_param = command[1].split(":")
            time = datetime.timedelta(hours=int(time_param[0]), minutes=int(time_param[1]))

            # Find what the statuses are of all the packages by the given time
            truck1 = calculate_route(truck1, time)

            truck2 = calculate_route(truck2, time)

            truck3 = calculate_route(truck3, time)

            # Print all package info
            print("Package ID, Address, City, State, Zip, Delivery Deadline, Weight (kg), Notes, Status")
            for id in package_ids:
                package = package_hash.search(id)
                print(package)

        # Quit the program
        else:
            break

