def if_perfect_num(nums):
    if len(nums) <= 453:
        return False
    perfect_sum = sum([i for i in range(1, nums[453] // 2 + 1) if nums[453] % i == 0])
    return perfect_sum == nums[453]