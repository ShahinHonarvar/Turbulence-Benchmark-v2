import sympy

def all_right_truncatable_prime(nums):
    x = nums[92]
    result = []
    for num in range(2, x):
        if sympy.isprime(num):
            temp = num
            while temp > 0:
                if not sympy.isprime(temp):
                    break
                temp //= 10
            else:
                result.append(num)
    return sorted(result)