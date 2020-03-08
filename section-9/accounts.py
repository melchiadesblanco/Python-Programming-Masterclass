import datetime
import pytz

class Account:
    """ Simple account class with balance """ 

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print('Account created for {}.'.format(self.name))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('You cannot withdraw that amount.')

    def show_balance(self):
        print('Balance is {}.'.format(self.balance))

if __name__ == '__main__':
    tim = Account('Tim', 0)
    tim.show_balance()
    tim.deposit(1000)
    tim.show_balance()
    tim.withdraw(2000)
    tim.show_balance()

