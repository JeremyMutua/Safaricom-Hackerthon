def main():
    pinCode = ["1234"]  # data of the account holders
    accountHoldersName = ["jeremy mutua"]
    accountNumber = ['0724836401']
    balance = 50000
    max_deposit_per_trans = 40000
    max_deposit_for_day = 150000
    max_withdrawal = 20000



    import sys

    print("Welcome to the Simple ATM")
    input("Press ENTER to continue")


    def another():
        answer = input("Would you like to make another transaction y/n?: ").lower()
        if answer == 'y':
            active = True
        else:
            active = False
            sys.exit("Thank you for using Simple ATM services")


    active = True

    while active:
        print("1: Deposit")
        print("2: Withdraw")
        print("3: Balance")
        print("4: Quit")

        option = int(input("What would you like to do: "))

        if option == 1:
            deposit = int(input("How much would you like to deposit: "))
            deposit_count = 1
            total_deposit = 0
            while deposit_count < 4:

                if deposit > max_deposit_per_trans or total_deposit > max_deposit_for_day:
                    print("Invalid amount")
                    break

                else:
                    print("You deposited Ksh." + str(deposit))
                    print(f"Balance:Ksh. {deposit+balance} ")
                    break
            balance = balance + deposit
            deposit_count += 1
            total_deposit += deposit

        elif option == 2:
            print("Your total amount available for withdrawal is: Ksh." + str(balance))
            withdrawal_count = 0
            total_withdrawal = 0
            while True:
                withdraw = int(input("Withdraw: Ksh."))
                if withdraw > max_withdrawal or withdrawal_count > 3:
                    print("Invalid Amount")
                    continue
                else:
                    print(f"You have withdrawn {withdraw}.")
                balance = balance - withdraw
                print(f"balance: {balance}")
                withdrawal_count += 1
                total_withdrawal += withdraw


                break
        elif option == 3:
            print("balance: Ksh." + str(balance))
        elif option == 4:
            value = input("Are you sure you want to quit? (y/n): ").lower()
            if value == "y":
                sys.exit("Thank you for using simple ATM services")
            else:
                continue
main()
