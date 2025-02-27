from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[39]
    result = []
    for num in range(2, x):
        if isprime(num):
            temp = num
            while temp > 0:
                if not isprime(temp):
                    break
                temp //= 10
            else:
                result.append(num)
    return sorted(result, reverse=True)