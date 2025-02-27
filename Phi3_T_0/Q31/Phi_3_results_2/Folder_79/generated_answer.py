def if_perfect_num(nums):
    if len(nums) > 63:
        return sum([i for i in range(1, nums[63]) if nums[63] % i == 0]) == nums[63]
    return False