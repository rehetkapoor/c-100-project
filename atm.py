class ATM:

    def __init__(self, cardNumber, pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber

newUser=ATM("461984", "3621")
newUser2=ATM("897321", "8436")
print(newUser.cardNumber)
print(newUser.pinNumber)

print(newUser2.cardNumber)
print(newUser2.pinNumber)