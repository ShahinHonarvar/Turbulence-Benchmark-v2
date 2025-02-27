from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[767]

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    primes = [i for i in range(2, x) if isprime(i) and '0' not in str(i)]
    left_truncatable_primes = [p for p in primes if is_left_truncatable_prime(p)]
    return sorted(left_truncatable_primes, reverse=True)