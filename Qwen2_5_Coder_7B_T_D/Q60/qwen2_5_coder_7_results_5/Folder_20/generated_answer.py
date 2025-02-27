from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[100]
    truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if isprime(num) and all((isprime(int(str_num[l:r])) for l in range(len(str_num)) for r in range(l + 1, len(str_num) + 1))):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)