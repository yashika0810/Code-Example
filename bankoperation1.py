print("Enter the OTP - 1234")
o = int(input("Enter the OTP"))
if o == 1234:
  print("Yes")
  print("Choose your preference!")
  print("NEW ACCOUNT, WITHDRAW, DEPOSIT, BALANCE INQUIRY, DEMAND DRAFT, CANCEL")
  pref = input("Enter your preference: ")
  if(pref == "NEW ACCOUNT"):
    name = input("Name: ")
    age = input("Age: ")
    addr = input("Address: ")
    cont = input("Contact Number: ")
    gend = input("Gender: ")
    print(f'ACCOUNT HOLDER DETAILS: \n Name:{name} \n Age:{age} \n Address:{addr} \n Contact:{cont} \n Gender:{gend}')
  elif(pref == "WITHDRAW"):
    amt = int(input('Enter the amount you want to withdraw'))
    print(amt)
    if amt <= 100 or amt >= 10000:
      print("LIMIT EXCEEDED")
    else:
      print("HERE IS YOUR MONEY!")

  elif(pref == "DEPOSIT"):
    dep = int(input("Enter the amount of deposit"))
    if(dep % 5 == 0):
      print("Money is deposited")
    else:
      print("Enter valid amount")
  elif(pref == "BALANCE INQUIRY"):
    print("Choose Deposit amount or Outstanding balance or Minimum Due Amount")
  elif(pref == "DEMAND DRAFT"):
    nbank = input("Name of Bank: ")
    nacc = input("Name of Account Holder: ")
    nbrch = input("Name of branch: ")
    tamt = input("Total Amount: ")
    print(f'DEMAND DRAFT:  \n Name of Bank: {nbank} \n Name of Account Holder: {nacc} \n Name of branch: {nbrch} \n Total Amount: {tamt}')
  else:
    print("CANCEL")


else:
  print("Sorry, Try again!")
