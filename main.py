# Andy Anderson (ID: 010837214)

import datetime
from package import Package
from truck import Truck
from utils import Utils

class Main:
  #initialization
  packageLoadouts = [
    [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27], #Truck 1
    [3, 13, 14, 15, 16, 18, 19, 20, 29, 30, 31, 34, 36, 37, 38, 40], #Truck 2
    [1, 6, 25, 28, 32, 33, 35, 39] #Truck 3
  ]

  packageCount = Package.initializePackages() #creates packages and adds them to hash table
  
  truck2 = Truck(2, packageLoadouts[1].copy(), datetime.timedelta(hours=8)) #load packages to truck 2 (copy needed to preserve original array for reference)
  truck2.deliverPackages()
 
  truck3 = Truck(3, packageLoadouts[2].copy(), datetime.timedelta(hours=9, minutes=5)) #load packages to truck 3 
  truck3.deliverPackages()

  truck1 = Truck(1, packageLoadouts[0].copy(), min(truck2.currentTime, truck3.currentTime)) #load packages to truck 1 (leaves when one of the drivers is available)
  truck1.deliverPackages()
  
  #menu
  Utils.underlinePrint("\nWelcome to Western Governors University Parcel Service (WGUPS)")
  while True:
    print("Please select your option:")
    print("1. View total distance traveled")
    print("2. View package attributes at given time")
    print("3. Quit application")
    try:
      inputSelection = int(input("\nEnter your selection: "))
      match inputSelection:

        case 1: #total distance traveled
          print()
          totalMileage = truck1.totalMileage + truck2.totalMileage + truck3.totalMileage #calcuate mileage of all trucks
          print(f"Total Distance Traveled: {totalMileage} Miles")

        case 2: #package statuses
          try:
            inputTime = input("Enter time to check package attributes. Please enter in format hh:mm:ss: ")
            h, m, s = inputTime.split(":")
            time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            try:
              inputPackage = input("Enter package ID to check attributes. To view all packages, enter \"all\": ")
              packagesToCheck = [] #stores package IDs to check. This is arguably the most readable way to do this without repeating code
              if inputPackage == "all": #all packages
                for packageID in range(packageCount): #loop through all package IDs
                  packagesToCheck.append(packageID + 1) #add package ID to array
              else: #only one package
                  packagesToCheck.append(int(inputPackage)) #add just the single package to package array
              for packageID in packagesToCheck: #check packages in array (either 1 or all)
                package = Package.packages.lookup(packageID) #get package object
                Utils.underlinePrint(f"\nPackage {packageID}") #prints package ID
                for attributeLine in package.getAllAttributes(time): #requirement b, returns all attributes
                  print(attributeLine) #prints attribute
            except:
              print("\nInvalid package input")
          except:
            print("\nInvalid time input")

        case 3: #quit
          print()
          break #stop loop
        
    except:
      print("\nInvalid selection")
    print()