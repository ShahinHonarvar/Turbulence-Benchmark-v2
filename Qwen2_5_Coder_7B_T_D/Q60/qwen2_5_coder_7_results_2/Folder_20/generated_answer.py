from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[100]
    primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and isprime(num):
            str_num = str(num)
            while len(str_num) > 1:
                if not (isprime(int(str_num[1:])) and isprime(int(str_num[:-1]))):
                    break
                str_num = str_num[1:-1]
            else:
                primes.append(num)
    return sorted(primes, reverse=True)