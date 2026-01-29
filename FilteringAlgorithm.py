# First we input our database
dataset = [
    {"name": "James", "class": "FC01", "exam score": 75, "coursework score": 45},
    {"name": "Natasha", "class": "FC02", "exam score": 95, "coursework score": 85},
    {"name": "Kumail", "class": "FC02", "exam score": 85, "coursework score": 75},
    {"name": "Tariq", "class": "FC01", "exam score": 75, "coursework score": 55},
    {"name": "Qimeng", "class": "FC01", "exam score": 80, "coursework score": 80},
    {"name": "Ming", "class": "FC02", "exam score": 90, "coursework score": 75}
]

# Then we create a robust FilteringAlgorithm that works with any dataset with a list of dictionaries
def Filtering_Algorithm(dataset):

    print("Welcome to the Filtering Algorithm! Input the key and value")

    #ask for key and value inputs
    key = input("What is the key?: ")
    value = input("What is the value?: ")

    results = []
    # create an empty list so we can store our results there

    for item in dataset:
        # go through every item in the dataset
        if key in item:
            # if the string form of the key in item matches the given string form of value
            if str(item[key]) == str(value):
                results.append(item)

    # we check to see if the results were empty, if it is empty then that means no item was found with the given key and value
    if results == []:
        print("No items found with that key and value.")
    else:
        #Print a header as filtered results
        print("Filtered results:")
        for item in results:
            #for every item in the filtered list
            print(item)
            #we print the item
    # Since I am demonstrating all of the different algorithms I will not write return however in future projects if I wish to reuse the answers I got I would use return.

#Call our function using 3 variables: Dataset, key and value

Filtering_Algorithm(dataset)

def Aggregation_Algorithm(dataset):
    #initialise our counters
    #key sum will take the sum of the key values
    key_sum=0
    #count will use a counter
    count=0
    print("Welcome to the Aggregation Algorithm! Input the key")
    
    #ask for key and value inputs
    key=input("What is the key: ")

    results = []
    # create an empty list so we can store our results there

    for item in dataset:
        # go through every item in the dataset
        if key in item:
            #then we see if our key is in that item if it is
            key_sum+=item[key]
            #we will sum the key values by adding all of the keys for each loop
            count+=1
            #and increment our counter for the formula of average=sum/length of sum

    #we check to see if the count is 0 because if it is 0 then that means the user inputted the wrong value and there is no items with that key
    if count==0:
        print("No items were found with the key")
    else:
        #if the count is not 0 then we will go ahead and print the results
        average=key_sum/count
        #average= sum/length of sum
        print(f"The average of the key {key} is: {average}")
        #print out our message

Aggregation_Algorithm(dataset)

def Sorting_Algorithm(dataset):
    print("Welcome to the Sorting Algorithm! Input the key")

    #we ask for the key
    key=input("What is the key?: ")

    #we will be using bubble sort to sort names and values that correspon to the key
    #first we define the list length as the same as the dataset
    list_length=len(dataset)
    #create our bubble sort algorithm
    for outer_index in range(list_length): #loop through the whole list_length (the length of the dataset)
        for inner_index in range(list_length -1): #compare each pair this loop goes through the list from the beginning to the second-to-last item.
            # read the current value and the next value for the chosen sort key
            current_value = dataset[inner_index][key] #Here we extract the value for the sorting key from each of the two neighbouring dictionaries.
            next_value = dataset[inner_index+1][key] #Examples: 1. if key = "name", values might be "James" and "Kumail" 2. If key = "exam score", values might be 75 and 90.
            
            #if the current value is greater than the next value, swap them. Example: for strings - alphabetical comparison (e.g., “Tariq” > “James”). 2.For strings: alphabetical comparison (e.g., “Tariq” > “James”).
            if current_value>next_value:
                
                temp=dataset[inner_index] # A temporary variable temp holds the first item.
                dataset[inner_index]=dataset[inner_index+1] #Then the second item moves into the first position.
                dataset[inner_index+1]=temp #Then the second item moves into the first position.
    
    #After the sorting is done, print the sorted results
    print(f"\n Sorted results by {key}: ") #This will print the results 
    for item in dataset: #This loops through the now-sorted dataset and prints each item.
        print(item) #print each dictionary

Sorting_Algorithm(dataset)