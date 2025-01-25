import datetime
import os

current_datetime = datetime.datetime.now()

print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)


current_date = datetime.datetime.now().date()

print(current_date)

print("Year:", current_date.year)
print("Month:", current_date.month)
print("Day:", current_date.day)



settime = datetime.datetime.now().time()

specific_date = datetime.date(2000, 3, 8)

print(specific_date.year)
print(specific_date.month)
print(specific_date.day)


future_date = current_datetime + datetimetimedelta(day=100)
past_date = current_datetime - datetimetimedelta(day=100)


print("100 days in future is:", future_date)
print("100 days in the past is:", past_date)

tekst = "World"
with open("text.txt", "w") as file:
    file.write("Hello", tekst)

file_path = "text.txt"
file = open(file_path, "r")

content = file.read()
print(content)
file.close()


with open("text.txt", "r") as file:
    lines = file.readlines()
    print(lines)


with open("text.txt", "r") as file:
    line = file.readline()
    print(line)


with open("text.txt", "a") as file:
    file.write("\nnew data appended")




if os.path.exists("text.txt"):
    print("file exists!")































