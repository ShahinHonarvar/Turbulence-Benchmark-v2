def if_perfect_num(nums):
    if len(nums) > 276 and is_perfect(nums[276]):
        return True
    return False

def is_perfect(n):
    sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_of_divisors == n