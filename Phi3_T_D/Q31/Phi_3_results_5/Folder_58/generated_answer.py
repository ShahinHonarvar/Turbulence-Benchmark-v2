def if_perfect_num(nums):
    if len(nums) > 714:
        return sum([i for i in range(1, nums[714]) if nums[714] % i == 0]) == nums[714]
    return False