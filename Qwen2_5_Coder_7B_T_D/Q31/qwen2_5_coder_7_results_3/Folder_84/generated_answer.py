def if_perfect_num(nums):
    return sum([i for i in range(1, nums[685]) if nums[685] % i == 0]) == nums[685]