from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[35]
    right_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        if all((isprime(int(str_num[:i])) for i in range(1, len(str_num) + 1))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)