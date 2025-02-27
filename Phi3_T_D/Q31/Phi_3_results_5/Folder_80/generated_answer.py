def if_perfect_num(nums):
    if len(nums) > 746:
        perfect_sum = sum([i for i in range(1, nums[746] // 2 + 1) if nums[746] % i == 0])
        return perfect_sum == nums[746]
    return False