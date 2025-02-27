from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[79]
    result = []
    for num in range(23, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            left = str_num
            while len(left) > 1:
                left = left[1:-1]
                if not isprime(int(left)):
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)