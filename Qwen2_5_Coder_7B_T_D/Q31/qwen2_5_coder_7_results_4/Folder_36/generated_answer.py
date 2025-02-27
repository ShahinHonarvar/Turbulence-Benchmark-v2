def if_perfect_num(nums):
    return sum([i for i in range(1, nums[990]) if nums[990] % i == 0]) == nums[990]