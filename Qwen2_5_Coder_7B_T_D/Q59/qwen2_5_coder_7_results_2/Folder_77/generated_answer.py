from sympy import primerange

def all_left_truncatable_prime(nums):
    x = nums[767]
    primes = list(primerange(2, x))
    left_truncatable_primes = []
    for num in primes:
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((int(str_num[:i]) in primes for i in range(1, len(str_num)))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)