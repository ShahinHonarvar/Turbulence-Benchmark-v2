from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[41]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and all((isprime(int(str(num)[:i])) and isprime(int(str(num)[i:])) for i in range(1, len(str(num))))):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)