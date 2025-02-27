from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[64]

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:-i])):
                return False
        return True

    def generate_primes(limit):
        primes = []
        for num in range(2, limit + 1):
            if isprime(num):
                primes.append(num)
        return primes
    primes = generate_primes(x)
    truncatable_primes = [p for p in primes if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)