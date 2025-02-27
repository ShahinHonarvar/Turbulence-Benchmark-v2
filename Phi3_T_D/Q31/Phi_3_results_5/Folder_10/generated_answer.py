def is_perfect(n):
    sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_of_divisors == n

def if_perfect_num(nums):
    if len(nums) > 54 and is_perfect(nums[54]):
        return True
    else:
        return False