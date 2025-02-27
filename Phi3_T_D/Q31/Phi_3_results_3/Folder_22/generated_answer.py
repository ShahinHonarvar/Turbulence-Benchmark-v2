def if_perfect_num(nums):
    if 72 < len(nums):
        return sum((i for i in range(1, nums[72] // 2 + 1) if nums[72] % i == 0)) == nums[72]
    return False