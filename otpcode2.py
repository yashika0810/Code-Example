import random as r
OTP=r.randint(1,20)
print('your otp is ',OTP)
first_name=input('enter your first name')
last_name=input('enter your last name')

attempt=0


while(attempt < 4):
    otp = int(input('enter your otp'))
    if otp==OTP:
        print("OTP SUCCESSFULLY MATCHED")
        raise SystemExit
    elif otp > 20 or otp < 1:
        print('wrong otp, please try again')

    else:
        print("ENTER THE OTP AGAIN")
        attempt=attempt+1
        a = input("Enter yes/no to continue - ")

        if a=='yes' :
            print(otp)
            continue
        elif a=='no':
            print('thanks for attempt')
            break
    if attempt==4:

        print('SORRY,PROGRAM CRASHED')

    break





