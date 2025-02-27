def if_perfect_num(nums):
    return sum([n for n in range(1, nums[42]) if nums[42] % n == 0]) == nums[42] if len(nums) > 42 else False