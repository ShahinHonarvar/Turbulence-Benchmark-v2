import math

def gcf_three_nums(nums):
    a = nums[341]
    b = nums[238]
    c = nums[374]
    return math.gcd(a, math.gcd(b, c))