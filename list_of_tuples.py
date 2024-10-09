'''
Using comprehension,create a new list of tuples from two given lists:

### sample calls

list1[1,2,3]
list2["mark","alice","john]

result: listOfTuple[(1,"mark"),(2,"alice"),(3,"john")] 
'''

# pseudocode
# make two lists
list1 = [1, 2, 3]
list2 = ["mark", "alice", "john"]

# make a list of tuples from two lists
list_of_tuples = [(list1[element], list2[element]) for element in range(len(list1))]

# print the list of tuples
print("listOfTuple{}".format(list_of_tuples))
