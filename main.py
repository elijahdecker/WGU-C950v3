from HashTable import HashTable
from Package import Package
import csv

if __name__ == '__main__':
    packageHash = HashTable()
    with open('packages.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], "at the hub")
            packageHash.insert(int(package.id), package)
    with open('distances.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            print(row[1].split('\n')[0])
