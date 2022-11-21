
class Account:

    def __init__(self,name: str)-> None:
        '''
        Constructor to create intial state of an account object.
        :param name: Account 's holder first name.
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self,amount) -> bool:
        '''
        Method to decrease balance.
        :param amount: float input
        :return: boolean status
        '''

        if amount >= 0: # avoid negative amount
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self,amount)-> bool:
        '''
        Method to increase the balance
        :param amount: float input
        :return: Boolean status
        '''

        if (amount > 0) or (amount < self.__account_balance): # ensure positive value and smaller than balance
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        '''
        Method to retrieve balance
        :return: float
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Method to get the account holder 's name.
        :return: string
        '''
        return self.__account_name

