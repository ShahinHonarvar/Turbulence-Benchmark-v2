from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[14]
    primes = []
    for num in range(1, x):
        if isprime(num) and '0' not in str(num):
            num_str = str(num)
            while num_str:
                if not isprime(int(num_str)):
                    break
                num_str = num_str[1:]
            else:
                primes.append(num)
    return sorted(primes, reverse=True)