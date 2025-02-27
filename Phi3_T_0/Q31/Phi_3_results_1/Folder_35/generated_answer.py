def if_perfect_num(nums):
    if len(nums) > 993:
        return sum([i for i in range(1, nums[993]) if nums[993] % i == 0]) == nums[993]
    return False