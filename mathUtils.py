#mathUtils.py:

def isPrime(num):
    if num < 2 or num % 2 == 0:
        return num == 2
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def largestPrimeFactor(num):
    if isPrime(num):
        return num

    i = 3
    while i < num / 2 + 1:
        if num % i == 0:
            f = num / i
            if isPrime(f):
                return 0
        i += 1
    return 0
