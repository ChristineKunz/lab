import pytest
from account import *

class Test:

    def setup_method(self):
        self.a1 = Account('001-John')

    def teardown_method(self):
        del self.a1


    def test_init(self):
        assert self.a1.get_name() == '001-John'
        assert self.a1.get_balance() == 0


def test_deposit():
    assert self.a1.deposit(1.0) == True
    assert self.a1.get_balance() == 1.0
    assert self.a1.deposit(-1) == False
    assert self.a1.get_balance() == 1.0
    assert self.a1.deposit(0) == False
    assert self.a1.get_balance() == 1.0

def test_withdraw():
    assert self.a1.withdraw(1.0) == False
    assert self.a1.get_balance() == 0
    assert self.a1.withdraw(-1) == False
    assert self.a1.get_balance() == 0
    self.a1.deposit(5)
    assert self.a1.withdraw(6) == False
    assert self.a1.get_balance() == 5
    assert self.a1.withdraw(4) == True
    assert self.a1.get_balance() == 1

