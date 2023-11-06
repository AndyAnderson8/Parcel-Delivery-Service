import datetime
from utils import Utils
from package import Package

class Truck:
  def __init__(self, id, packages, departTime):
    #initialize object attributes
    self.id = id
    self.packages = packages #initializes packages into truck
    self.currentTime = departTime #keeps track of current time in the truck as it makes deliveries
    self.totalMileage = 0 #starts day with no miles
    self.speed = 18 #average miles per hour
    self.currentAddress = "4001 South 700 East" #Hub at WGU

    #updates status for all loaded packages that it is now "enroute"
    for packageID in packages:
      package = Package.packages.lookup(packageID) #initialized to first package in list
      package.truckID = self.id
      package.setStatus("En Route", self.currentTime) # "At Hub" to "En Route"

  #function to deliver all packages and update their status
  def deliverPackages(self):
    while len(self.packages) > 0: #continues until there are no more packages in truck

      #package 9 will be updated at 10:20 with new address
      if 9 in self.packages: 
        if self.currentTime >= datetime.timedelta(hours=10, minutes=20): #info unknown until 10:20
          packageObj = Package.packages.lookup(9) #get package to be updated
          if packageObj.address != "410 S State St":
            packageObj.address = "410 S State St" #fixing wrong address
            packageObj.zip = "84111"

      #algorithm to pick next package to deliver
      nextPackage = Package.packages.lookup(self.packages[0]) #initialized to first package in list
      for packageID in self.packages:
        packageObj = Package.packages.lookup(packageID) #gets package object from ID
        if Utils.distanceBetween(self.currentAddress, packageObj.address) < Utils.distanceBetween(self.currentAddress, nextPackage.address): #sees if next package is closer than the closest one already checked
          nextPackage = packageObj #updated because distance to this package is shorter
      deliveryMileage = Utils.distanceBetween(self.currentAddress, nextPackage.address) #calculate distance between location and next delivery
      deliveryTime = datetime.timedelta(hours = (deliveryMileage / self.speed)) #delivery time is distance / speed
      self.totalMileage += deliveryMileage #milage of delivery added
      self.currentAddress = nextPackage.address #truck is now at the location of previous delivery
      self.currentTime += deliveryTime #time of day advances to time of delivery
      self.packages.remove(nextPackage.id) #remove package from truck
      nextPackage.setStatus("Delivered", self.currentTime)
      nextPackage.deliveryTime = self.currentTime