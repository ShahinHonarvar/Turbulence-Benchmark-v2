def if_perfect_num(nums):
    return nums[453] == sum([i for i in range(1, nums[453]) if nums[453] % i == 0])