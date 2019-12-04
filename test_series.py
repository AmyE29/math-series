from series import Fibonacci, Lucas, sum_series

def test_Fibonacci_0():
    expected = 0
    actual = Fibonacci(0)
    assert actual == expected

def test_Fibonacci_1():
    expected = 1
    actual = Fibonacci(1)
    assert actual == expected

def test_Fibonacci_2():
    expected = 1
    actual = Fibonacci(2)
    assert actual == expected

def test_Fibonacci_3():
    expected = 2
    actual = Fibonacci(3)
    assert actual == expected

def test_Fibonacci_4():
    expected = 3
    actual = Fibonacci(4)
    assert actual == expected

def test_Fibonacci_5():
    expected = 5
    actual = Fibonacci(5)
    assert actual == expected

def test_Fibonacci_6():
    expected = 8
    actual = Fibonacci(6)
    assert actual == expected

def test_Fibonacci_7():
    expected = 13
    actual = Fibonacci(7)
    assert actual == expected

# Testing for Lucas numbers
def test_Lucas_0():
    expected = 2
    actual = Lucas(0)
    assert actual == expected

def test_Lucas_1():
    expected = 1
    actual = Lucas(1)
    assert actual == expected

def test_Lucas_2():
    expected = 3
    actual = Lucas(2)
    assert actual == expected

def test_Lucas_3():
    expected = 4
    actual = Lucas(3)
    assert actual == expected

def test_Lucas_4():
    expected = 7
    actual = Lucas(4)
    assert actual == expected

def test_Lucas_5():
    expected = 11
    actual = Lucas(5)
    assert actual == expected

def test_Lucas_6():
    expected = 18
    actual = Lucas(6)
    assert actual == expected

def test_Lucas_7():
    expected = 29
    actual = Lucas(7)
    assert actual == expected

# sum_series tests
def test_Series_1():
    expected = 13
    actual = sum_series(7)
    assert actual == expected


def test_Series_2():
    expected = 18
    actual = sum_series(6, 2, 1)
    assert actual == expected


def test_Series_3():
    expected = 29
    actual = sum_series(7, 2, 1)
    assert actual == expected
# testing with different optional parameters and getting an un-Lucas and un-Fibonacci result.
def test_Series_4():
    expected = 58
    actual = sum_series(7, 4, 2)
    assert actual == expected


