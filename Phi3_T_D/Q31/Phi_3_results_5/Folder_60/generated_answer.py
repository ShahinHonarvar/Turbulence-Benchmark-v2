def if_perfect_num(nums):
    if len(nums) > 88 and all((num > 0 for num in nums)):
        return sum((i for i in range(1, nums[88]) if nums[88] % i == 0)) == nums[88]
    else:
        return False