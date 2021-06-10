# emelu codes
from tabulate import tabulate

print("***Welcome to EM BANK***")
# bank information
balance: float = 10500000.00
account = "EasySavings"
chance = 5
# return assign
restart = "Y"
while chance >= 0:
    user_pin = int(input("ENTER PIN XXXX: "))
    if user_pin == 2004:
        print("PIN VALID")
        while restart not in ("n", "no", "N", "No", "NO"):
            print("Press 1 to view your balance")
            print("Press 2 to make a withdraw")
            print("Press 3 to send money")
            print("Press 4 to pay bills")
            option = int(input("Choose your operation: "))
            if option == 1:
                print("Your balance is ", balance)
                restart = input("Would your like to do another transaction")
                if restart in ("n", "no", "N", "No", "NO"):
                    print("Thank you, take your card")
                    break
            elif option == 2:
                option2 = 'y'
                # had to create an atm kinda look(using tabulate)
                withdraw = [["Amount(NGN)", "Amount(NGN)", ], ["1,000.00", "20,000.00"], ["5,000.00", "50,000.00"],
                            ["10,000.00", "Other amount <50,000.00(1)"], ]
                print(tabulate(withdraw, headers='keys', tablefmt='fancy_grid'))
                withdraw = float(input("How much are you withdrawing"))
                if withdraw in [1000, 5000, 10000, 20000, 50000, 100000]:
                    balance = balance - withdraw
                    print("Transaction successful")
                    restart = input("Would your like to do another transaction")
                    if restart in ("n", "no", "N", "No", "NO"):
                        print("Thank you, take your card")
                        break
                elif withdraw != [1000, 5000, 10000, 20000, 50000, 100000]:
                    print("Invalid amount /nPlease try again")
                    restart = 'y'
            elif option == 3:
                rec_actno: int = int(input("Enter recipient account number"))
                ask = input("Savings or Current")
                table = [["Amount(NGN)", "Amount(NGN)", ], ["1,000.00", "20,000.00"], ["5,000.00", "50,000.00"],
                         ["10,000.00", "Other amount <50,000.00(1)"], ]
                print(tabulate(table, headers='keys', tablefmt='fancy_grid'))
                send_money = float(input("How much would you link to send"))
                if send_money in [1000, 5000, 10000, 20000, 50000, 100000]:
                    balance = balance - send_money
                    restart = input("Would your like to do another transaction")
                    if restart in ("n", "no", "N", "No", "NO"):
                        print("Thank you, take your card")
                        break
            elif option == 4:
                bills = [["1. Pay bills", " 2. Pay bills", ], ["3. Buy Credit", "4. Buy Data"],
                         ["5. Buy post-paid token", "6. Buy pre-paid token"], ]
                print(tabulate(bills, headers='keys', tablefmt="fancy_grid"))
                bills = int(input("Which bill are you choosing? "))
                if bills == 1:
                    print("Visit: https://www.quickteller.com/pay-bills ")
                elif bills == 2:
                    print("Visit: https://www.recharge.com/en/nigeria ")
                elif bills == 3:
                    print("Visit: https://www.quickteller.com/pay-bills ")
                elif bills == 4:
                    print("Visit: https://www.quickteller.com/pay-bills ")
                elif bills == 5:
                    print("Visit: https://www.quickteller.com/pay-bills ")
                elif bills == 6:
                    print("Visit: https://www.quickteller.com/pay-bills ")
                print("Check the web for confirmation, Thanks")
                restart = input("Would your like to do another transaction")
                if restart in ("n", "no", "N", "No", "NO"):
                    print("Thank you, take your card")
                    break
    else:
        if user_pin != 2004:
            print("WRONG PIN")
            chance = chance - 1
            if chance == 0:
                print("NO MORE TRIES, CONTACT YOUR BANK")
                break
