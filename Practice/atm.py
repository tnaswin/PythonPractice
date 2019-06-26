
class Bank:

    def transaction(self):
        balance = int(input("Enter current balance : "))
        print("Your current balance is: %d" %balance)
        withdraw = int(input("Enter amount to withdraw : "))
        if withdraw > 0 and withdraw < balance:
            if withdraw % 5 == 0:
                balance = balance - (withdraw + 0.50)
            else:
                print("Amount should be a multiple of 5.")
        else:
            print("Insufficient balance.")
        print("New balance: %0.2f" %balance)


if __name__=="__main__":
    b = Bank()
    b.transaction()
