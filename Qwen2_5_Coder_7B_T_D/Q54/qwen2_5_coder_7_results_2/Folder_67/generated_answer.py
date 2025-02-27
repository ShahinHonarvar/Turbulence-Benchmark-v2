from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[71]
    right_truncatable_primes = []
    for num in range(2, x):
        is_right_truncatable = True
        temp = num
        while temp > 0:
            if not isprime(temp):
                is_right_truncatable = False
                break
            temp //= 10
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)