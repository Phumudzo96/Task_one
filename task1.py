#create three new variables and give them values
num1 = 4
num2 = 0
num3 = 9

#i'm going to compare num1 with num2 and see which number is bigger than the other
if num1 > num2:
    print(num1)
else:
    print(num2)

#now i'm going to find out if num1 is an odd or even number
if num1 % 2 == 0:
    print("Num1 is an even number")
else:
    print("Num1 is an odd number")

#now im going to see which variable is the largest, smallest and the middle value
if (num3 > num1) and (num3 > num2):
    print(num3)
if (num1 > num3) or (num1 > num2):
    print(num1)
if (num2 < num1) and (num2 < num3):
    print(num2)

