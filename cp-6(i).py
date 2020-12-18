"""
WAP to find the factorial of a number using recursion technique.
"""


def recursion_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursion_factorial(n - 1)


num = int(input('Enter a number: '))
if num < 0:
    print('Sorry, Factorial does not exit for negative number')
elif num == 0:
    print('The Factorial of 0 is 1')
else:
    print('The Factorial of ', num, ' is ', recursion_factorial(num))
