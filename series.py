def Fibonacci(n):
    # First Fibonacci number is 0
    if n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    # The value of the current index is the value of the two previous indicies added together.
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# writing the Lucas numbers function
def Lucas(n):
    # First Lucas number is 2
    if n==0:
        return 2
    # Second Lucas number is 1
    elif n==1:
        return 1
    # The value of the current index is the value of the two previous indicies added together.
    else:
        return Lucas(n-1)+Lucas(n-2)

def sum_series(n, x=0, y=1):
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n-2, x, y) + sum_series(n-1, x, y)

