#creating an empty list
my_list = []
print( "The list I have created is of type",type(my_list))
#appending the following values into my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("This is the result after appending elements into an empty list", my_list)
#inserting value 15 at position 2
my_list.insert(1 ,15)
print("I am now inserting value '15' in the second position in the list",my_list)
#extending the existing list with the new list
new_list = [50,60,70]
my_list.extend(new_list)
print("The original list is now extendend by anothe list of values 50,60,70",my_list)
#removing the last element from the list
my_list.remove(my_list[-1])
print("This is what I get after removing the last value in the list",my_list)
#sorting list in ascending order
my_list.sort()
print("List is now sorted in ascending order",my_list)
#printing out the index of value 30
index = my_list.index(30)
print("value '30' has an index of ",index ,"in my list")