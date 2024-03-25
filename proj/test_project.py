from project import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar = Jar(0)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(10)
