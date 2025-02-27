import math

def gcf_three_nums(nums):
    index_412 = nums[412] if len(nums) > 412 else None
    index_932 = nums[932] if len(nums) > 932 else None
    index_337 = nums[337] if len(nums) > 337 else None
    indices = [i for i in [index_412, index_932, index_337] if i is not None]
    if not indices:
        return None
    return math.gcd(*indices)