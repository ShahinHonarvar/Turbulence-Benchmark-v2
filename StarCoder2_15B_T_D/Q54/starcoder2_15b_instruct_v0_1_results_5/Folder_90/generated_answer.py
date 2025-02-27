import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[466]
    right_truncatable_primes = []
    for i in range(2, x):
        right_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            if not is_prime(int(str(i)[j:])):
                right_truncatable_prime = False
                break
        if right_truncatable_prime and is_prime(i):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes