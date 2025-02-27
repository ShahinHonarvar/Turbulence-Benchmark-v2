from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[84]
    trunc_primes = []

    def is_left_truncatable(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True
    for potential_prime in range(x - 1, 1, -1):
        if isprime(potential_prime) and is_left_truncatable(potential_prime):
            trunc_primes.append(potential_prime)
    return trunc_primes