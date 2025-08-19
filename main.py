import random
import sys

ten_to_ten, ten_to_eleven = 10**10, 10**11
#Create a unique account number
def checker(account_number):    
    with open('Account_numbers.txt', 'r') as file:
        file.seek(0)
        lines = file.read().split('\n')
        for line in lines:
            if line == account_number:
                checker(random.randint(ten_to_ten, ten_to_eleven))   
        return(account_number)

def account_checker(customer_account_number):
    line_number=0
    with open("Bank_Data.txt", "r") as f:
        f.seek(0)
        for i in f:
            line_number+=1
            line = i.strip()
            account_number, name, credit = line.split(",")
            if(int(account_number)==int(customer_account_number)):
                return(True,line_number)
        print("Account not Found, Try Again")
        return(False,None)
            
print("WELCOME to Shashwat Bank of Interest!!!!\n\n")
reply=input("Enter A to Access your Account or Enter M to make a new Account: ")
if reply=='M':
    print("Please wait a sec...")
    account_number=checker(random.randint(ten_to_ten, ten_to_eleven))
    name=input("Enter your name: ")
    print("Your Account Number is: ",account_number,"\n Please save it for Acceesing your account.....")
    credit=int(input("Enter minimum 10000 to open your Account: "))
    if credit>=10000:
        with open('Account_numbers.txt','a') as f:
            f.write(f"{account_number}\n") 
        data=()
        print("Please wait we are saving your Account details....")
        data= f"{account_number},{name},{credit}\n"
        with open("Bank_Data.txt","a") as f:
            f.write(data)
        print("Your Account has been created--")
    else:
        print("Minimum balance 10000 is required to create new Account, try again.... \n")
elif(reply.upper() == "A"):
    count_number=0
    customer_account_number =int(input("Enter your Number: "))
    bol,line_number=account_checker(customer_account_number)
    if bol==True:
        
        operation= input("Enter C to Credit Money or D to Debit money:- ")
        if(operation.upper()=="C"):
            with open("Bank_Data.txt", "r") as file:
                lines = file.readlines()

            # Convert to zero-based index
            line_number -= 1  

            account_number, name, balance = lines[line_number].strip().split(",")
            credit = int(input("Enter Amount to be credited: "))
            balance = int(balance) + credit
            print("Your new Balance is :",int(balance))
            lines[line_number] = f"{account_number},{name},{balance}\n"

            with open("Bank_Data.txt", "w") as file:
                file.writelines(lines)
        elif(operation.upper()=="D"):
            with open("Bank_Data.txt", "r") as file:
                lines = file.readlines()

            # Convert to zero-based index
            line_number -= 1  

            account_number, name, balance = lines[line_number].strip().split(",")
            debit = int(input("Enter Amount to be Debit: "))
            balance = int(balance) - debit
            if(balance<0):
                print("Transaction not possible")
                sys.exit()
            print("Your new Balance is :",int(balance))
            lines[line_number] = f"{account_number},{name},{balance}\n"

            with open("Bank_Data.txt", "w") as file:
                file.writelines(lines)
    elif(bol==False):

        sys.exit()
