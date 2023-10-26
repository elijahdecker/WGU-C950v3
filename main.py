import datetime

from HashTable import HashTable
from Package import Package
from Truck import Truck
import csv

package_hash = HashTable()
with open('packages.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        p = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], "at the hub")
        package_hash.insert(int(p.id), p)
with open('distances.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    distances = list(reader)
def find_address(address):
    i = 0
    for col in distances[0]:
        if address in col:
            return i
        i = i + 1
def calculate_route(truck):
    undelivered_packages = truck.packages
    while len(undelivered_packages) > 0:
        least_distance = 1000.0
        next_package = None
        for package_id in undelivered_packages:
            curr_loc = int(find_address(truck.current_location))
            # print(str(curr_loc) + " line 30")
            package = package_hash.search(package_id)
            next_loc = int(find_address(package.address))
            # print(str(next_loc) + " line 32")
            # print(distances[next_loc])

            if (next_loc > curr_loc):
                distance = float(distances[next_loc][curr_loc])
            else:
                distance = float(distances[curr_loc][next_loc])
            # print(str(package_id))
            # print(str(distance) + " line 34")

            if (distance < least_distance):
                next_package = package
                least_distance = distance
        undelivered_packages.remove(int(next_package.id))
        truck.current_location = next_package.address
        print(str(least_distance) + " id:" + str(next_package.id))



if __name__ == '__main__':

    truck1 = Truck("Truck 1", 18, datetime.time(8), [1, 13, 14, 15, 16, 19, 20, 29, 30, 34, 37, 40], "4001 South 700 East")
    calculate_route(truck1)
    truck2 = Truck("Truck 2", 18, datetime.time(9, 15), [3, 6, 18, 36, 38], "4001 South 700 East")

    truck3 = Truck("Truck 3", 18, datetime.time(10, 30), [9, 25, 28, 32], "4001 South 700 East")

