from sympy import isprime

def all_left_truncatable_prime(nums):

    def is_left_truncatable_prime(n):
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    x = nums[36]
    truncatable_primes = []
    for num in range(2, x):
        if isprime(num) and '0' not in str(num) and is_left_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)