class Account:
    '''CLASS ATTRIBUTES'''
    # outside of an any instance method
    # shared among all instances of a class
    # can be changed on any instance, or entire class
    # User.bank_name = 'First National'
    # cupid.bank_name = 'First National'
    bank_name = 'First National North Pole'
    currency = 'candy canes'
    count = 0
    has = []
    def __init__(self, name, first, last):
        self.name = name
        self.first_name = first.capitalize()
        self.last_name = last.capitalize()
        self.balance = 0
        Account.has.append(self)
        Account.count += 1
    
    '''CLS METHODS'''
    @classmethod
    # MUST have @classmethod
    def get_class_info(cls):
        print(f'\nWelcome to the {cls.bank_name}!')
        print(f'Here the currency is in {cls.currency}.')
        print(f'There are {cls.count} accounts here.')
        return [print(f'{i.last_name} {i.first_name}, {i.name}') for i in cls.has]



'''READ'''
Account.get_class_info()


##################################################
#                   TERMINAL                     #
##################################################
# Welcome to the First National North Pole!
# Here the currency is in candy canes.
# There are 0 accounts here.