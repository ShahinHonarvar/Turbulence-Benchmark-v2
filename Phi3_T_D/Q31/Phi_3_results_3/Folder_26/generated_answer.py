def if_perfect_num(nums):
    if 222 < len(nums):
        return sum([x for x in range(1, nums[222]) if nums[222] % x == 0]) == nums[222]
    return False