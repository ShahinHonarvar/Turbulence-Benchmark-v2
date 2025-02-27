def if_perfect_num(nums):
    if len(nums) < 46:
        return False
    target = nums[45]
    summation = sum([i for i in range(1, target) if target % i == 0])
    return summation == target