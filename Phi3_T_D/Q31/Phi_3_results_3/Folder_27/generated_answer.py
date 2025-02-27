def if_perfect_num(nums):
    return not nums or (len(nums) >= 57 and sum((i for i in range(1, int(nums[56]) + 1) if nums[56] % i == 0)) == nums[56] * 2)