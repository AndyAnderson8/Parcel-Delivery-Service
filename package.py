import datetime
from hashtable import HashTable
from utils import Utils

class Package:
  packages = HashTable() #empty hash table to initialize

  def __init__(self, id, address, city, state, zipcode, deadline, weight):
    self.id = id
    self.address = address
    self.city = city
    self.state = state
    self.zipcode = zipcode
    self.deadline = deadline
    self.weight = weight
    self.truckID = None
    self.statusHistory = [] #will store as [[status, update time], [status, update time], [status, update time]]

  #adds new status to package status history
  def setStatus(self, status, time):
    self.statusHistory.insert(0, [status, time]) #newest updates go to the front
  
  #returns most recent status before given time
  def getStatus(self, time):
    for statusUpdate in self.statusHistory: 
      if statusUpdate[1] <= time: #get most recent status that has already happened before time
        return statusUpdate

  #loads all packages to be stored in hashtable (packages class variable)
  def initializePackages():
    packageCount = 0
    packageData = Utils.parseCSV("CSVs/packages.csv")
    for package in packageData: #organizing lines from csv into respective attributes
      id = int(package[0].strip())
      address = package[1].strip()
      city = package[2].strip()
      state = package[3].strip()
      zipcode = package[4].strip()
      deadline = package[5].strip()
      if deadline == "EOD": #can't store end of day as "EOD"
        deadline = datetime.timedelta(hours=23, minutes=59, seconds=59) #last second of day
      else:
        split = deadline.split(" ")[0].split(":")
        h = int(split[0])
        m = int(split[1])
        if "PM" in deadline:
          h += 12 #add 12 hrs to AM time
        deadline = datetime.timedelta(hours=h, minutes=m)
      weight = int(package[6].strip())
      packageObj = Package(id, address, city, state, zipcode, deadline, weight)
      packageObj.setStatus("At Hub", datetime.timedelta(hours=0, minutes=0, seconds=0)) #initial status
      Package.packages.insert(id, packageObj) #popualte hash table
      packageCount += 1
    return packageCount
  
  #gets package info for given time and returns it, used to satisfy requirement B
  def getAllAttributes(self, time):
    status = self.getStatus(time) #get final status for package at time
    return [
      f"Destination: {self.address}, {self.city}, {self.state} {self.zipcode}",
      f"Weight: {self.weight} kilos",
      f"Delivery Deadline: {self.deadline}",
      f"Transit Vehicle: Truck {self.truckID}",
      f"Current Status: {status[0]} (Updated: {status[1]})"
    ]