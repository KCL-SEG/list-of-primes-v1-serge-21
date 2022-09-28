"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    i = 0
    while len(list) < number_of_primes:
        if isPrime(i):
            list.append(i)
        i += 1
    return list

def isPrime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True