def if_perfect_num(nums):
    if len(nums) > 97:
        return sum([i for i in range(1, nums[97]) if nums[97] % i == 0]) == nums[97]
    return False