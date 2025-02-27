import math

def gcf_three_nums(nums):
    index90 = 90 % len(nums) if 90 >= len(nums) else 90
    index54 = 54 % len(nums) if 54 >= len(nums) else 54
    index96 = 96 % len(nums) if 96 >= len(nums) else 96
    return math.gcd(math.gcd(nums[index90], nums[index54]), nums[index96])