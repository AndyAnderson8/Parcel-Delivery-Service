class HashTable:
  def __init__(self, length=20): #20 is somewhat arbitrary
    self.kvs = [] #key-values
    for i in range(length):
      self.kvs.append([]) #initializes empty array of given length

  #insert or update key-value pair into hash table
  def insert(self, key, item):
    index = hash(key) % len(self.kvs)
    found = False
    for kv in self.kvs[index]:
      if kv[0] == key:
        found == True
        kv[1] = item #updates item
        break
    if not found:
      self.kvs[index].append([key, item]) #insert item

  #delete key-value pair from hash table if found
  def remove(self, key):
    index = hash(key) % len(self.kvs)
    for kv in self.kvs[index]:
      if kv[0] == key:
        self.kvs[index].remove(kv) #removes key-value pair
        break
  
  #get value from key in hash table
  def lookup(self, key):
    index = hash(key) % len(self.kvs)
    for kv in self.kvs[index]:
      if kv[0] == key:
        return kv[1] #returns value
    return None 