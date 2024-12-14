from lesson7.user import print

try:
    result = 10/0
    print(result)
except:
      print("Oops, Tried devidind by zero")


fruits = {
    "apple" :5
    "mango" : 7
     "banana" : 9
}

try:
    print(fruits["cherry"])

except KeyError:
    print("This Key does not exist")



    text = "This is not a number"


    try:
        text_to_int = int(text)

    except Exception as e:
        print("An erorr occured", e)




try:
    result = 10/2
except:
      print("Oops, Tried devidind by zero")
else:
    print("The division was sucsesful", result)



try:
    result = 10/2
except:
      print("Oops, Tried devidind by zero")
finally:
    print("Finally the result was executed", result)













