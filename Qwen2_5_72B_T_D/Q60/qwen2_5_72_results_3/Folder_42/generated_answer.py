from sympy import isprime

def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(n):
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])) or not isprime(int(str(n)[:-i])):
                return False
        return True
    x = nums[64]
    primes = [i for i in range(2, x + 1) if isprime(i) and '0' not in str(i)]
    truncatable_primes = [p for p in primes if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)