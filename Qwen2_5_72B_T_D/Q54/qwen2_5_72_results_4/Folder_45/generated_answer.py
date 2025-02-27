from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[61]
    right_truncatable_primes = []

    def generate_right_truncatable_primes(n):
        if n > x:
            return
        if isprime(n):
            right_truncatable_primes.append(n)
            for d in range(1, 10):
                generate_right_truncatable_primes(n * 10 + d)
    for start in [2, 3, 5, 7]:
        generate_right_truncatable_primes(start)
    return sorted(right_truncatable_primes)