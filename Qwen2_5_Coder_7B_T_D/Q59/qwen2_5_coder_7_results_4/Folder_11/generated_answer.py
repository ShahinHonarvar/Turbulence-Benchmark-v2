import sympy

def all_left_truncatable_prime(nums):
    x = nums[86]
    primes = sympy.primerange(2, x)
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' not in str_prime:
            all_left_primes = all((sympy.isprime(int(str_prime[:i])) for i in range(1, len(str_prime) + 1)))
            if all_left_primes:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)