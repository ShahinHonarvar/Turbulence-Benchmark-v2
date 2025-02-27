import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_primes(numbers):
    limit = numbers[31]
    primes = [str(i) for i in range(2, limit + 1) if is_prime(i)]

    def is_truncatable(n):
        n = str(n)
        if len(n) == 1 or len(n) == 2:
            return is_prime(int(n)) and (len(n) == 1 or len(n) == 2)
        return all((is_prime(int(n[i:])) and is_prime(int(n[:len(n) - i])) for i in range(1, len(n))))
    return sorted([int(p) for p in primes if is_truncatable(p)], reverse=True)