from functools import *

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print("This is a function using functools module to calculate Fibonacci sequence.")
try:
    n = int(input("Please enter a number(<=100):"))
    if n > 100:
        raise ValueError("Invalid input")
except ValueError as e:
    print(e)
    exit()
else:
    for i in range(n):
        item = fib(i + 1)
        if item <= 2147483647:
            print(f"Item {i + 1} : {item}")
        elif 2147483647 < item <= 9223372036857775808:
            print(f"\033[0;31;40mItem {i + 1} : {item}\033[0m")
        else:
            print(f"\033[0;32;40mItem {i + 1} : {item}\033[0m")

    
