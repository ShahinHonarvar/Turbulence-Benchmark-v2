def if_perfect_num(nums):
    if len(nums) < 7:
        return False
    perfect_sum = sum((i for i in range(1, nums[6]) if nums[6] % i == 0))
    return perfect_sum == nums[6]