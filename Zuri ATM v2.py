import random
import sys
import datetime
import time

UserRegister = {}
def Welcome():
    print('Welcome to Lorem Bank ')
    while True:
        try:
            Options = int(input('''
1. Existing Account
2. New Account\n'''))
            if (Options == 1):
                login()
                break
            elif (Options == 2):
                register()
                break
            else:
                print('Invalid Option')
                continue
        except ValueError:
            print('Invalid Input')


def register():
    print('\tCREATE ACCOUNT')
    Fname = input('Enter First name:\n')
    Lname = input('Enter Last name: \n')
    YoB = input('Enter year of birth: ')
    MoB = input('Enter month of birth: ')
    DoB = input('Enter day of birth: ')
    NiN = input("Enter your NIN: ")
    acctBal = 0.00
    
    while True:
        createPin = (input('create pin: \n'))
        CheckPin = (input('confirm pin: \n'))
        if len(createPin) < 4:
            print('Password must contain atleast 4 characters')
            continue

            register()
            break
        else:
            if (CheckPin == createPin):
                
                AcctNum = str(AcctNumGen())
            
                print("Account Created")
                print(f'Account number: {AcctNum}')
                UserRegister[AcctNum] = [Fname, Lname, YoB, MoB, DoB, createPin,
                                                 acctBal]
                print('Login below')

                login()
                break

                
            else:
                print('passwords do not match')
                continue


def login():
    print('\n ===== LOGIN =====')
    for item in range(1, 3):
        EnterAcctNum = input('Enter Account number: \n')
        EnterPin = input('Enter pin: \n')
        if ((EnterAcctNum in UserRegister)):
            if (EnterPin == UserRegister[EnterAcctNum][5]):
                
                

                now = datetime.datetime.now()
                print('\n you are logged in at :')
                print(now.strftime("%d/%m/%Y %H:%M:%S"))

                Banking(EnterAcctNum)
                break
            else:
                print("UserID provided doesn't match")
                continue
        else:
            print('Invalid account number')
            forgottenID = input('forgotten userID? (press 1), tap enter to skip \n')
            if (forgottenID == '1'):
                ForgotPin()
            elif (len(forgottenID) == 0):
                Welcome()
            else:
                print('invalid input')
                sys.exit()
    login()


def ForgotPin():
    print('''Please provide your KYC documents to a Lorem representative.


          ''')
    Welcome()


def AcctNumGen():
    print('Your account Number is')
    return random.randrange(0000000000, 9999999999)


def Banking(user):
  


    print('''
    select option
    1. Withdraw
    2. Deposit
    3. Complaint
    4. Account Balance
    5. Log out
    6. Exit''')
    ChooseOption = int(input('Choose option: '))
    if ChooseOption == 1:
        withdraw(user)
    if ChooseOption == 2:
        deposit(user)
    if ChooseOption == 3:
        complaint(user)
        Back2Banking(user)

    if ChooseOption == 4:
        account_balance(user)
    if ChooseOption == 5:
        print('are you sure you want to log out?')
        logOut = input("1.(yes) 2(no) \n")
        if logOut == '1':
            
            login()
        elif logOut == '2':
            Banking(user)
        else:
            print('Invalid option')
            Banking(user)

    if ChooseOption == 6:
        exit()


def deposit(user):
    print('====== DEPOSIT CASH ======')
    DepositAmt = float(input('amount to be deposited: \n #'))
    DepositPin = (input('Input tranasaction pin => \n'))
    if DepositPin == UserRegister[user][5]:
        print('Deposit succesful')
        
        print('\n Transaction successful')
        UserRegister[user][6] = UserRegister[user][6] + DepositAmt
        Back2Banking(user)
        
    else:
        
        print('Invalid pin, Transaction Failed')
        
        Banking(user)


def withdraw(user):
    print( '\t-----WITHDRAW CASH-----')
    WithdrawAmt = float(input('input amount to withdraw => \n #'))
    if WithdrawAmt <= UserRegister[user][6]:
        WithdrawPin = (input(' Enter Transaction pin => \n'))
        if WithdrawPin == UserRegister[user][5]:
            print('\n Withdrawal successful')
            UserRegister[user][6] = UserRegister[user][6] - WithdrawAmt
            Back2Banking(user)

        else:
            
            print('Invalid pin, Transaction Failed')
            
            Banking(user)

    else:
        print('processing...')
        
        print('Insufficient Funds')
        
        Back2Banking(user)

def complaint(user):
    print("We are sorry for your incovenience")
    error=input("Please enter your complaint here: ")
    print("We will get right on it!")
          
def account_balance(user):
    print('\tACCOUNT BALANCE ')
    
    
    print("Your account balance is,",'#', UserRegister[user][6])
    Back2Banking(user)


def Back2Banking(user):
    while True:
        transaction_two = input('''\n would you like to make another action?
1(yes to proceed)
2 (No to exit)\n''')
        if transaction_two == '1':
            
            Banking(user)
            break
        if transaction_two == '2':
            exit()
        else:
            print('invalid Option')
            continue


Welcome()
