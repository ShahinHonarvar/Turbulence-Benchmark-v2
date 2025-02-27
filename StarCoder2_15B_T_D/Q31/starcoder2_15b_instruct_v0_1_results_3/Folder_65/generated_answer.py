def if_perfect_num(nums):
    total = 0
    for i in range(1, nums[35] // 2 + 1):
        if nums[35] % i == 0:
            total += i
    return total == nums[35]