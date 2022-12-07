print("enter the first number")
x = input()
print("enter the second number")
y = input()
print("enter 1 for addition, 2 for substruction, 3 for multiplication and 4 for division")
z = input()

if (z == "1") :
    s = int(x) + int(y)
    w = "addition"
elif (z == "2") :
    s = int(x) - int(y)
    w = "subtraction"
elif (z == "3") :
    s = int(x) * int(y)
    w = "multiplication"
else :
    s = int(x) / int(y)
    w = "division"

print("the result of", w, "is", s)