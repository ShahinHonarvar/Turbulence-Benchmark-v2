def is_perfect_num(nums):
    if len(nums) <= 99:
        return False
    perfect_sum = sum([i for i in range(1, nums[99]) if nums[99] % i == 0])
    return perfect_sum == nums[99]