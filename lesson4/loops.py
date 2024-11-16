#while loop

count = 1 #initislizes the loop control variable

while count <= 5 #The condition if count is less than or equal to 5
    print("Literation", count)
    count +=1 #Increment the loop control variable




#DO WHILE LOOP

#infinite loop


while True:
    #promt user to enter a positive number
    user_input = input("enter a positive number:")


#checks if the inputn is nuymeric

if user_input.isnumeric():
    number = int(user_input)

    if number > 0:
        break


    print("invalid input please try again")

    print("You have entered a valid positive number", number)





list = [1,2,3,4,5,6,7]
target =4

for number in list:
    print(number)
    if number == target:
        print("Target found")
        break #End the loop immediatly after findong the target





























