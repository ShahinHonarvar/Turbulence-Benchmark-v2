from sympy import isprime

def all_left_right_truncatable_prime(nums):
    return sorted([num for num in nums if is_left_right_truncatable_prime(num)], reverse=True)

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(len(str_num)):
        if not isprime(int(str_num[i:])):
            return False
        if not isprime(int(str_num[:len(str_num) - i])):
            return False
    return True