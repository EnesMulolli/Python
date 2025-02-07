import datetime
import os

# Getting current datetime
current_datetime = datetime.datetime.now()
print("Current Date and Time:")
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)

# Getting current date
current_date = datetime.date.today()
print("\nCurrent Date:")
print("Year:", current_date.year)
print("Month:", current_date.month)
print("Day:", current_date.day)

# Creating a specific date
specific_date = datetime.date(2000, 3, 8)
print("\nSpecific Date:")
print("Year:", specific_date.year)
print("Month:", specific_date.month)
print("Day:", specific_date.day)

# Calculating future and past dates
future_date = current_datetime + datetime.timedelta(days=100)
past_date = current_datetime - datetime.timedelta(days=100)
print("\nFuture Date (100 days from now):", future_date)
print("Past Date (100 days ago):", past_date)

# Writing to a file
tekst = "World"
with open("text.txt", "w") as file:
    file.write("Hello " + tekst)

# Reading from the file
file_path = "text.txt"
with open(file_path, "r") as file:
    content = file.read()
    print("\nContent of text.txt:")
    print(content)

# Appending new data to the file
with open("text.txt", "a") as file:
    file.write("\nNew data appended")

# Reading all lines from the file
with open("text.txt", "r") as file:
    lines = file.readlines()
    print("\nAll lines from text.txt:")
    for line in lines:
        print(line.strip())  # Strip removes newline characters

# Checking if file exists
if os.path.exists("text.txt"):
    print("\nFile 'text.txt' exists!")

