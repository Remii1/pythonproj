class Bankaccount:
    balance = 2000

    def deposit(self):
        print(200)
    def withdraw(self):
        print(600)
    def check (self):
        print(600)
    def transfer(self):
        print(900)

class interestaccount(Bankaccount):
      def interest(self):
          print(500)
      def deposit(self):
          print(900)

class chargingaccount(Bankaccount):
      def fee(self):
          print(468)
      def withdraw(self):
          print(890)

it =interestaccount()
it.deposit()
it.withdraw()
it.check()
it.transfer()
ch = chargingaccount()
ch.fee()
ch.withdraw()






