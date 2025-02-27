from itertools import takewhile

def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
            if not is_prime(int(str(n)[:-i])):
                return False
        return True
    x = numbers[55]
    primes = list(takewhile(lambda v: v <= x, filter(is_prime, range(2, x + 1))))
    result = [prime for prime in primes if is_truncatable_prime(prime)]
    return sorted(result, reverse=True)