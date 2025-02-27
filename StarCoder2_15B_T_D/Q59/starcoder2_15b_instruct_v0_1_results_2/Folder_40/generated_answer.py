import re

def all_left_truncatable_prime(argument):
    argument = re.findall('\\(([^)]*)\\)', argument)[0]
    argument = tuple(map(int, argument.split(', ')))
    x = argument[10]

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = []
    for i in range(2, x):
        n = i
        while n:
            if not is_left_truncatable_prime(n):
                break
            n //= 10
        else:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)