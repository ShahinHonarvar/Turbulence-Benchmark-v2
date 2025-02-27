import math

def gcf_three_nums(nums):
    if len(nums) < 102:
        raise ValueError('The provided list does not contain an index 91')
    a, b, c = (nums[91], nums[45], nums[48])
    return math.gcd(math.gcd(a, b), c)