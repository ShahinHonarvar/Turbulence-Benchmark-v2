from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[64]
    left_right_truncatable_primes = []
    primes = set()

    def is_left_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if '0' in str_n[i:]:
                return False
            if not isprime(int(str_n[:i + 1])) or not isprime(int(str_n[i:])):
                return False
        return True

    def sieve(limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for start in range(2, int(limit ** 0.5) + 1):
            if is_prime[start]:
                for multiple in range(start * start, limit + 1, start):
                    is_prime[multiple] = False
        for num in range(2, limit + 1):
            if is_prime[num]:
                primes.add(num)
    sieve(x)
    for prime in primes:
        if is_left_right_truncatable(prime):
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)