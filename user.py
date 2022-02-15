######################################################
'''            CLASS AND INSTANCES OF             '''
#                - define a class                    #
#               - CLASS ATTRIBUTES                   #
#               - constructor method                 #
#              - DEFAULT PARAMETERS                  #
#            - update class parameters               #
#         - saving instances as has to Object        #
#               - instance methods                   #
#                - static methods                    #
#         - GET ANOTHER INSTNACE'S value             #
#            - instantiate a class                   #
#        - INSTANTIATE MULTIPLE classes at once      #
#              - call class methods                  #
'''              TERNARY OPERATOR                  '''
'''return True if (balance - amount > 0) else False'''
#                -XTINA.CODES-                       #
######################################################
from account import Account

class User: 
# keyword class,  define name (upper cammel)
    ################
    '''ATTRIBUTES'''
    ################    
    currency = 'candy canes'
    count = 0
    has = []
    # [<__main__.User object at 0x0000020A1269FFD0>, <__main__.User object at 0x0000020A1269FEB0>, <__main__.User object at 0x0000020A1269FE50>]
    def __init__(self, first_name, last_name, email):
        # CONSTRUCTOR built in method
        # gets called when object is built
        # constructor(PARAMETERS)
        # SELF is a representation of the INSTANCE not class
        # IMPLICIT PASSAGE OF SELF: don't need to pass as argument
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.email = email
        self.accounts_has = []
        # save user's accounts in a list of classes
        # default balance of 0
        '''DEFAULT CLASS PARAMETERS'''
        # must be declared below
        # adds to class properties when instatiated
        # ClassName.variable_name = value
        User.count += 1     
        '''add an object to another object'''
        # 1) create a variable in the holding object
        #    usually a list ex: has =[]
        # 2) append object isntance to holding object variable
        User.has.append(self)
        
        
        
    #############
    '''METHODS'''
    #############
    '''useful tools'''
    def talk_to_me(self):
        return f"Which account {[f'({i}) {self.accounts_has[i].name}, Balance : {self.accounts_has[i].balance}' for i in range( len(self.accounts_has) )]}? "


    def validate_account(self, e): # pass input value
        # 1) get a list of user's accounts
        while e not in [i for i in range( len(self.accounts_has) )]:
        # 2) while input is not in list of user's accounts
            print('Invalid entry... Try one of these integars:')
            e = int(input( self.talk_to_me() ))
            # try input again
        return e # return proper input value
    
    
    '''INSTANCE METHODS'''
    # derived from specific instance
    # always use self
    ''' create '''
    def create_account(self, e):
        new = Account(e, self.first_name, self.last_name)
        # 1) new instance of Account class
        self.accounts_has.append(new)
        # 2) append instance to constructor property (accounts_has)
        [print(f'Congrats on your new {i.name} account') for i in self.accounts_has] 
        # 3) access constructor for accounts_has (list of dictionaries)
        return self
    
    
    ''' read '''
    def get_info(self):
        print(f'\nHello {self.last_name}, {self.first_name}')
        print(f'Email: {self.email}')
        [print(f'{i.name.capitalize()} : {i.balance}') for i in self.accounts_has]
        
        return self
    
    
    ''' update / edit '''    
    def deposit(self, e):
        print(f'\nI see you are trying to deposit {e} {self.currency}...')
        lets_talk = self.validate_account( int(input( self.talk_to_me() )) )
        # 1) validate user input
        self.accounts_has[lets_talk].balance += e
        # 2) update balance on account 
            # using dict format
            # index is input value
            # amount is element from param
        print(f'New Balance: {self.accounts_has[lets_talk].balance} {self.currency}') 
        #3)  show new balance
        return self
    
    
    def withdraw(self, e):
        print(f'\nI see you are trying to withdraw {e} {self.currency}...')
        lets_talk = self.validate_account( int(input( self.talk_to_me() )) )
        # 1) validate user input
        ''' static methods need call Class.method() because they don't implicitly have access'''
        if User.validate_withdraw(self.accounts_has[lets_talk].balance, e):
        # 2) check to see if balance in account will be positve after transaction
            self.accounts_has[lets_talk].balance -= e
            print(f'New Balance: {self.accounts_has[lets_talk].balance} {self.currency}')
            # 3a) show user validated balance
        else:
            print(f'{self.first_name}, we are unable to witdraw {e} {self.currency} from {self.accounts_has[lets_talk].balance} {self.currency}.')
            # 3b) show user how validation numbers do not align
        return self
    
    
    def transfer(self, to_user, amount):
        print(f'\nI see you are trying to transfer {amount} {self.currency} to {to_user.first_name}...')
        lets_talk = self.validate_account( int(input( self.talk_to_me() )) )
        # 1) validate user input
        ''' static methods need call Class.method() because they don't implicitly have access'''
        if User.validate_withdraw(self.accounts_has[lets_talk].balance, amount):
        # 2) check to see if balance in account will be positve after transaction
            self.accounts_has[lets_talk].balance -= amount
            to_user.accounts_has[0].balance += amount
            print(f'New Balance: {self.accounts_has[lets_talk].balance} {self.currency}')
            # 3a) show user validated balance
        else:
            print(f'{self.first_name}, we are unable to witdraw {amount} {self.currency} from {self.accounts_has[lets_talk].balance} {self.currency}.')
            # 3b) show user how validation numbers do not align
        return self
    
    
    '''STATIC METHOD'''
    # doesn't use class information
    # just completes general functions    
    def validate_withdraw(balance, amount):
        return True if (balance - amount > 0) else False
    
    
    '''CLS METHODS'''
    @classmethod
    def get_class_info(cls):
        print(f'\nThere are {cls.count} clients at {Account.bank_name}')
        for i in cls.has:
            print(f'\nMeet {i.first_name} {i.last_name}...')
            print(f'Email: {i.email}')
            for j in i.accounts_has:
                print(f'{j.name} : {j.balance}')
        
        
        
'''CREATE / INSTANTIATE'''
santa, mrs_claus, cupid = User('santa', 'claus', 'hohoho@northpole.com'), User('Misses', 'Clause', 'themrs@northpole.com'), User('cupid', 'valentines', 'cupidsarrow@valentines.com')
santa.create_account('checking').create_account('saving')
mrs_claus.create_account('checking').create_account('saving')
# print( santa.accounts_has[0].name)

'''UPDATE / CALL METHODS'''
# santa.deposit(50)
# santa.withdraw(10)
# santa.transfer(mrs_claus, 10)
mrs_claus.get_info()
Account.get_class_info()
User.get_class_info()



##################################################
#                   TERMINAL                     #
##################################################


# Congrats on your new checking account
# Congrats on your new checking account
# Congrats on your new saving account
# Congrats on your new checking account
# Congrats on your new checking account
# Congrats on your new saving account

# Hello Clause, Misses
# Email: themrs@northpole.com
# Checking : 0
# Saving : 0
# Welcome to the First National North Pole!
# Here the currency is in candy canes.
# There are 4 accounts here.
# Claus Santa, checking
# checking : 0
# saving : 0

# Meet Misses Clause...
# Email: themrs@northpole.com
# checking : 0
# saving : 0

# Meet Cupid Valentines...
# Email: cupidsarrow@valentines.com
# PS C:\Users\xtina\OneDrive\UnicornMagic\3. Python New> python -u "c:\Users\xtina\OneDrive\UnicornMagic\3. Python New\1. Fundamentals\Classes Play\classes_with_class.py"
# Congrats on your new checking account
# Congrats on your new checking account
# Congrats on your new saving account
# Congrats on your new checking account
# Congrats on your new checking account
# Congrats on your new saving account

# I see you are trying to deposit 50 candy canes...
# Which account ['(0) checking, Balance : 0', '(1) saving, Balance : 0']? 9
# Invalid entry... Try one of these integars:
# Which account ['(0) checking, Balance : 0', '(1) saving, Balance : 0']? 0
# New Balance: 50 candy canes

# I see you are trying to withdraw 10 candy canes...
# Which account ['(0) checking, Balance : 50', '(1) saving, Balance : 0']? 1
# Santa, we are unable to witdraw 10 candy canes from 0 candy canes.

# I see you are trying to transfer 10 candy canes to Misses...
# Which account ['(0) checking, Balance : 50', '(1) saving, Balance : 0']? 0
# New Balance: 40 candy canes

# Hello Clause, Misses
# Email: themrs@northpole.com
# Checking : 10
# Saving : 0

# Welcome to the First National North Pole!
# Here the currency is in candy canes.
# There are 4 accounts here.
# Claus Santa, checking
# Claus Santa, saving
# Clause Misses, checking
# Clause Misses, saving

# There are 3 clients at First National North Pole

# Meet Santa Claus...
# Email: hohoho@northpole.com
# checking : 0
# saving : 0

# Meet Misses Clause...
# Email: themrs@northpole.com
# checking : 0
# saving : 0

# Meet Cupid Valentines...
# Email: cupidsarrow@valentines.com