class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

        def start(self):
            print("started")

        def stop(self):
            print("stopped")

        def accelerate(self):
            print("accelerating...")
        
                    
        def change_gear(self, gear_type):
            print("gear changed")

            audi = Car("A6", "red", "audi", 80)

            print(audi.start())




audi = Car("A6", "red", "audi", 80)

print(audi.start())



class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is $0 :(")

    def withdrawl(self,amount):
        new_amount = 0 - amount
        print("you have withdrawn "+str(amount) +". Your remaining balance is "+ str(new_amount))

    def main():
        Card_number = input("insert your card number:- ")
        pin_number = input("enter your pin number:- ")

        new_user = Atm(Card_number , pin_number)

        print("Choose your activity ")
        print("1. Balance Enquiry   2. withdrawal")
        activity = int(input("enter activity number :-"))
        
        if (activity == 1):
            new_user.check_balance()
        elif (activity == 2):
                amount = int(input("enter the amount:-"))
                new_user.withdrawal(amount)
                else:
                    print("You can't withdraw that much money fool")

                    if __name__ == "__main__":
                        main()

