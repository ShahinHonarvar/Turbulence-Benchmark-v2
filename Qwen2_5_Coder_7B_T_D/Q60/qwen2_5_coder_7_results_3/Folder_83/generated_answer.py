from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[24]
    primes = [2, 3, 5, 7]
    left_right_truncatable_primes = []
    for num in range(11, x + 1):
        if isprime(num):
            str_num = str(num)
            if '0' not in str_num:
                if all((isprime(int(str_num[:i])) and isprime(int(str_num[-i:])) for i in range(1, len(str_num)))):
                    left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)