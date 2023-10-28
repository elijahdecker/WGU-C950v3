import datetime

from HashTable import HashTable
from Package import Package
from Truck import Truck
import csv

package_hash = HashTable()
package_ids = []
with open('packages.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    packages = list(reader)
with open('distances.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    distances = list(reader)

def populate_package_hash():
    for row in packages:
        p = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], "At the hub")
        package_ids.append(int(p.id))
        package_hash.insert(int(p.id), p)
def find_address(address):
    i = 0
    for col in distances[0]:
        if address in col:
            return i
        i = i + 1
def calculate_route(truck, time):
    undelivered_packages = truck.packages.copy()
    end_time = time
    # Do not run if the truck will not have departed
    if (end_time >= truck.current_time):
        # Change the status of each package on the truck to "En route"
        for package_id in truck.packages:
            package = package_hash.search(package_id)
            package.status = "En Route by " + truck.name
        while len(undelivered_packages) > 0:
            least_distance = 1000.0
            next_package = None
            for package_id in undelivered_packages:
                curr_loc = int(find_address(truck.current_location))
                package = package_hash.search(package_id)
                next_loc = int(find_address(package.address))

                if (next_loc > curr_loc):
                    distance = float(distances[next_loc][curr_loc])
                else:
                    distance = float(distances[curr_loc][next_loc])

                if (distance < least_distance):
                    next_package = package
                    least_distance = distance

            undelivered_packages.remove(int(next_package.id))
            truck.current_time = truck.current_time + datetime.timedelta(hours=(least_distance / truck.speed))
            if (truck.current_time > end_time):
                truck.current_time = end_time
                break;
            next_package.status = "Delivered @ " + str(truck.current_time)
            package_hash.insert(int(next_package.id), next_package)
            truck.current_location = next_package.address
            truck.distance += least_distance
            # print(str(least_distance) + " id:" + str(next_package.id))
    return truck



if __name__ == '__main__':


    while True:
        populate_package_hash()
        truck1_packages = [1, 13, 14, 15, 16, 19, 20, 23, 29, 30, 31, 34, 37, 40]
        truck1 = Truck("Truck 1", 18, datetime.timedelta(hours=8), truck1_packages, "4001 South 700 East")
        truck2_packages = [2, 3, 4, 5, 6, 10, 18, 21, 22, 26, 35, 36, 38]
        truck2 = Truck("Truck 2", 18, datetime.timedelta(hours=9, minutes=15), truck2_packages, "4001 South 700 East")
        truck3_packages = [7, 8, 9, 11, 12, 17, 24, 25, 27, 28, 32, 33, 39]
        truck3 = Truck("Truck 3", 18, datetime.timedelta(hours=10, minutes=30), truck3_packages, "4001 South 700 East")

        print("\n=============================================================================\n" +
              "p: Show all package information and total mileage\n" +
              "s {package_id} {time (ex: 13:10)}: Show single package information with time\n" +
              "a {time (ex 13:10)}: Show all packages with time\n" +
              "q: Exit program\n" +
              "=============================================================================")
        command = input("\ncommand: ").split(" ")
        if command[0] == "p":
            time = datetime.timedelta(hours=23)

            truck1 = calculate_route(truck1, time)

            truck2 = calculate_route(truck2, time)

            truck3 = calculate_route(truck3, time)

            print("Package ID, Address, City, State, Zip, Delivery Deadline, Weight (kg), Notes, Status")
            for id in package_ids:
                package = package_hash.search(id)
                print(package)
            print("Distance traveled: " + str(round(truck1.distance + truck2.distance + truck3.distance, 2)))
        elif command[0] == "s":
            if (len(command) < 3):
                print("Please provide both parameters")
                continue
            package_id = int(command[1])
            time_param = command[2].split(":")

            time = datetime.timedelta(hours=int(time_param[0]), minutes=int(time_param[1]))

            truck1 = calculate_route(truck1, time)

            truck2 = calculate_route(truck2, time)

            truck3 = calculate_route(truck3, time)

            print("Package ID, Address, City, State, Zip, Delivery Deadline, Weight (kg), Notes, Status")
            package = package_hash.search(package_id)
            print(package)
        elif command[0] == "a":
            if (len(command) < 2):
                print("Please provide a time")
                continue
            time_param = command[1].split(":")

            time = datetime.timedelta(hours=int(time_param[0]), minutes=int(time_param[1]))

            truck1 = calculate_route(truck1, time)

            truck2 = calculate_route(truck2, time)

            truck3 = calculate_route(truck3, time)

            print("Package ID, Address, City, State, Zip, Delivery Deadline, Weight (kg), Notes, Status")
            for id in package_ids:
                package = package_hash.search(id)
                print(package)
        else:
            break

