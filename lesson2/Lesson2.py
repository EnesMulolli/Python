fruits = ["apple","banana","cherry"]
print(fruits)

#create a tuple
words = ("spam","eggs","sausages")
print(words[1])

#creating a tuple with information about a person

person = ('Enes', 16 , "Student")
name, age , profession = person

print(name, "is a",profession," and he is ", age,"years old")

#creating a dictionary

my_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key2": "value2",
}
#more keys more values pair

contact_info = {
    "Blerta": "444-123123123",
    "Drini": "444-321321321"
}
#create a variable called enes's phone and use [] we can specify which keywe want to accses

enes_phone = contact_info ["Drini"]
print(enes_phone)
print(contact_info)

contact_info ["Blerta"] = "444-98989888"
print(contact_info)

#We want to add another friend to contact_info

contact_info ["Eros"] = "999-5556667"
print(contact_info)

#Delete a contact info
del contact_info ["Blerta"]
print(contact_info)

#Print oly the keys in the dictionary

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

#print items

items = contact_info.items()

print(items









