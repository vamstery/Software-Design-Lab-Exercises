# Function to display hashtable
def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("---", end = " ")
            print(j, end = " ")
              
        print()

HashTable = [[] for _ in range(10)]
  

def Hashing(keyvalue):
    return keyvalue % len(HashTable)
  

def insert(Hashtable, keyvalue, value):
      
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)
  

insert(HashTable, 10, 'Wina')
insert(HashTable, 25, 'Pau')
insert(HashTable, 20, 'Joms')
insert(HashTable, 19, 'Mars')
insert(HashTable, 9, 'Jackie')
insert(HashTable, 11, 'Ron')
insert(HashTable, 1, 'Nabs')
insert(HashTable, 2, 'Mike')
insert(HashTable, 21, 'Alex')
insert(HashTable, 21, 'Chit')
  
display_hash (HashTable)