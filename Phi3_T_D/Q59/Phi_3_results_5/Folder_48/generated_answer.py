import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(tup):
    x = tup[835]
    truncatable_primes = []

    def is_left_truncatable(number):
        str_num = str(number)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True
    for number in range(2, x):
        if is_left_truncatable(number):
            truncatable_primes.append(number)
    return truncatable_primes