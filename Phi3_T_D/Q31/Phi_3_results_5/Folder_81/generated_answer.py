def if_perfect_num(nums):
    if len(nums) < 21:
        return False
    return sum((i for i in range(1, nums[20]) if nums[20] % i == 0)) == nums[20]