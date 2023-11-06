import csv

class Utils:
  addresses = None #initially empty because needs to be parsed from CSV
  distances = None #initially empty because needs to be parsed from CSV

  #reads data from CSV into a list
  def parseCSV(dir):
    with open(dir) as file:
      return list(csv.reader(file))

  #gets the distance between two addresses
  def distanceBetween(address1, address2): #addresses -> ids -> distances
    if Utils.addresses == None: #if not yet initialized
      Utils.addresses = Utils.parseCSV("CSVs/addresses.csv") #initialize
    if Utils.distances == None: #if not yet initialized
      Utils.distances = Utils.parseCSV("CSVs/distances.csv") #initialize

    addressIDs = []
    for address in Utils.addresses:
      if address[2] == address1 or address[2] == address2:
        if address1 == address2:
          return 0 #no distance to deliver second package to the same address
        addressIDs.append(int(address[0]))
      if len(addressIDs) == 2: #done looking for IDs
        break 
    distance = Utils.distances[addressIDs[0]][addressIDs[1]] #try to get address from table
    if distance == "": #indexed in wrong order
      distance = Utils.distances[addressIDs[1]][addressIDs[0]] #tries alternate order
    return float(distance) 
  
  #prints string and underline for it
  def underlinePrint(string):
    print(string) #print string
    print("‾" * len(string.strip())) #print underline