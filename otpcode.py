import random as r
FName = input("Enter your first Name")
LName = input("Enter your last Name")
x = r.randint(1,20)
print("The OTP is",x)
count = 0
while (count < 4):
  UNum = int(input("Enter your OTP"))
  if UNum > 20 or UNum < 1:
    print("Wrong Input, Try Again!!")
    break
  else:
    if UNum == x:
      print("OTP successfully Matched!!")
      break
    else:
      print("Error! Enter the OTP Again!")
      count = count + 1
  if(count == 4):
    print("SORRY PROGRAM CRASHED")
