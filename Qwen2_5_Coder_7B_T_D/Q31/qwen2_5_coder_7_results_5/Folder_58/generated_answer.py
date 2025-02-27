def if_perfect_num(nums):
    return nums[714] == sum([i for i in range(1, nums[714]) if nums[714] % i == 0])