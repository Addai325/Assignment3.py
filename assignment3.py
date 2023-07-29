#Week Three(3)  Python Assignment
#Name: Ransford Addai
#Training ID: 32524



#QUESTION ONE(1)
#Write a code to find the second largest number in a list of integers after sorting the list
numbers = [10,5,20,15,8]
numbers.sort()
second_largest = numbers[-2]
print(second_largest)


#QUESTION TWO(2)
#Write a code to find the common elements between two lists of integers
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
common_elements = list(set(list1).intersection( set(list2)))
print(common_elements)


#QUESTION THREE(3)
#Write a code to create a new list with only the even numbers from the original list
numbers =[1,2,3,4,5,6,7,8]
even_numbers = [x for x in numbers if x % 2==0]
print(even_numbers)


#QUESTION FOUR(4)
#Create a tuple of even numbers and write python code to reverse the elements
Even_numbers = (2,4,6,8,10)
reversed_numbers = Even_numbers[::-1]
print(reversed_numbers)


#QUESTION FIVE(5)
#Create a tuple of even integers including duplicates and write Python code to create a new tuple with only the unique elements, removing duplicates
even_integers = (2,4,6,2,8,10,6,20,8)
new_integers = tuple(set(even_integers))
print(new_integers)


#QUESTION SIX(6)
#Create a tuple of odd integers including duplicates and write Python code to create a new tuple with only the unique elements, removing duplicates
odd_integers = (1,3,5,7,3,9,1,7,15)
new_odd_integers = tuple(set((odd_integers)))
print(new_odd_integers)


#QUESTION SEVEN(7)
#Create a code to find the union of two sets
set1 = {1,2,3}
set2 = {3,4,5}
Union_of_set = set1.union(set2)
print(Union_of_set)


#QUESTION EIGHT(8)
#Create a code to find the common elements between two sets of integers
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
common_elements = set1.intersection(set2)
print(common_elements)


#QUESTION NINE(9)
#Generate a new set with only the even numbers from the original set using Python Code
original_set = {1,2,3,4,5,6,7,8}
new_set = {x for x in original_set if x%2 == 0}
print(new_set)


#QUESTION TEN(10)
#Write a code to create a dictionary from two lists, one for keys and another for values
keys = ["name", "age", "city"]
values = ["John", 30, "New York"]
my_Dict = dict(zip(keys, values))
print(my_Dict)



