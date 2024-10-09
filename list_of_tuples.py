'''
Using comprehension,create a new list of tuples from two given lists:

### sample calls

list1[1,2,3]
list2["mark","alice","john]

result: listOfTuple[(1,"mark"),(2,"alice"),(3,"john")] 
'''

# pseudocode

# Define a class that takes two lists as input
class ListOfTuples:
    # Define a method that takes two lists as input
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2
    
    # Define a method that creates a list of tuples from two lists
    def create_list_of_tuples(self):
        list_of_tuples = [(self.list_1[element], self.list_2[element]) for element in range(len(self.list_1))]
        # Print the list of tuples
        print("listOfTuple{}".format(list_of_tuples))

# Make two lists
list1 = [1, 2, 3]
list2 = ["mark", "alice", "john"]

# Instantiate the class and call the method
tuple1 = ListOfTuples(list1, list2)
tuple1.create_list_of_tuples()
