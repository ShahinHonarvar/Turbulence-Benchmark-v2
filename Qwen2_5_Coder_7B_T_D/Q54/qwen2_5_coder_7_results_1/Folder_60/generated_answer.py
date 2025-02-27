from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[87]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            temp_num = num
            while temp_num > 0:
                if not isprime(temp_num):
                    break
                temp_num //= 10
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)