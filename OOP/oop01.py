import re
class UserMail():
    def __init__(self, login, email):
        self.login = login
        self.__email = email
    def get_email(self):
        return self.__email
    def set_email(self, email):
        if re.search("[\w'._=-]+@[\w'._=-]+$", email):
            self.__email = email
        else:
            "Нет специальных символов"
    email = property(fget=get_email, fset=set_email)

e = UserMail('sssss','eeee@.com')
e.email = 'eeee@ds.co@m'
print(e.email)
e.email = 'dddddddddddd@....c'
print(e.email)


class BankAccount():
    def __init__(self, name, balance):
        self.name = name 
        self.__balance = balance
    
    @property
    def my_balance(self):
        print("Get balance")
        return self.__balance
    
    @my_balance.setter
    def my_balance(self, value):
        print("Set balance")
        if not isinstance(value, (int, float)):
            raise ValueError()
        self.__balance = value
    @my_balance.deleter
    def delete_balance(self):
        print("delete balance")
        del self.__balance
    
    
    # my_balance = property()
    # my_balance = my_balance.getter(get_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(delete_balance)

    #balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

b1 = BankAccount('Misha', 200)

print(b1.my_balance)
b1.my_balance = 300
print(b1.my_balance)