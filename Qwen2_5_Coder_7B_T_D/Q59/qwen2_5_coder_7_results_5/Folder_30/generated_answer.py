from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[37]
    primes = [i for i in range(2, x) if str(i).count('0') == 0 and is_prime(i)]
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if all((is_prime(int(str_prime[:i])) for i in range(1, len(str_prime)))):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)