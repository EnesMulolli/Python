#create a set using curly braskets

#my_set = {1, 2, 3}
#print(my_set)

#creating a set from a list using the set() function

#my_set = ([4,5,6])
#print(my_set)

#create an empty set using the set() function
#my_set = set()
#print(my_set)


my_set = {1,1,2,4,4,5,6,3,3,2}
print(my_set)#Set will automaticlly remove duplicates



set1 = {1,2,3}
set2 = {3,4,5}

#union between set1 and 2 usintg the union() method

union_method = set1.union(set2)

#compute an union between set1 and set2 using the | operator

union_operator = set1 | set2

print("Union of set1 and set2 using method:",union_method)
print("union of set1 and set2 using the operator:", union_operator)

#compute intersection between set1 and set2 using the intersection() method

intersection_method = set1.intersection(set2)

#compute intersection between set1 and set2 using & operative

intersection_operator = set1 & set2
print("intersection of set1 and set2 using the intersection method:", intersection_method)
print("intersection of set1 and set2 using the intersection operator:", intersection_operator)



difference_method = set1.difference(set2)

#computing elementsthat are unique to set1 using the operator
difference_operator = set1 - set2

print("Difference of set1 and set2 using the difference method:", difference_method)
print("Difference of set1 and set2 using the - operator:", difference_operator)


#Computing the elements that are in set1 and set2 but not in their intersection
symetric_difference_method = set1.symmetric_difference(set2)

#computing the elements that are in set1 and set2 but not in their intersection using the ^operator
symetric_difference_operartor = set1 ^ set2

print("Symmetric difference of set1 and set2 using the symmetric difference method:", symetric_difference_method)
print("Symmetric difference of set1 and set2 using the symmetric difference operator:", symetric_difference_operartor)


# set methods

#create a set

my_set1 = {1,2,3}

#add number 7 at the end of the set

my_set1.add(7) #add method

#remove nuumber 3 from my set

my_set1.remove(3)#remove methot

#removing 8 from the set withot throwing and error if 8 in now on the set

my_set1.discard(8)
print(my_set1)

#removing all numbers from the set
my_set1.clear()

print(my_set1)



#remove duplications from a list

#create a list that contains duplications

my_list = [1,2,2,2,3,4,4,4,5,6]

#convert this list to a set to remove duplicatios

unique_set = set(my_list)
print(unique_set)

#convert this set to a list

unique_list = list(unique_set)
print(unique_list)


#Checking for common elements

blertas_interest = {"music", "movies", "travel"}
drilons_interests = {"movies", "games", "skiing"}

common_interests = blertas_interest.intersection(drilons_interests)
print(common_interests)


#in operator

colors = {"red", "green", "yellow","blue"}
color = "grey"
print(color in colors)





















