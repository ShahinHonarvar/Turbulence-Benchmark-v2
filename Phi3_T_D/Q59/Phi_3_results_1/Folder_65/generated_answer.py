from functools import reduce

def all_left_truncatable_prime(numbers):
    max_number = numbers[32]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, primes):
        str_n = str(n)
        while str_n:
            if not is_prime(n):
                return False
            n = int(str_n) // 10
            str_n = str(n)
        return True
    primes = [p for p in range(2, max_number) if is_prime(p)]
    truncatable_primes = []
    for prime in primes:
        if is_truncatable_prime(prime, primes):
            truncatable_primes.append(prime)
    return truncatable_primes