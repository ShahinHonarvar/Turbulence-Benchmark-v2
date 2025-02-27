def if_perfect_num(nums):
    if len(nums) > 59:
        return sum((i for i in range(1, nums[59]) if nums[59] % i == 0)) == nums[59]
    else:
        return False