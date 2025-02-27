def if_perfect_num(nums):
    perfect = sum([i for i in range(1, min(nums[632], 631)) if nums[632] % i == 0]) == nums[632]
    return perfect