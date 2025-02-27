def if_perfect_num(nums):
    total = 0
    for i in range(1, nums[162]):
        if nums[162] % i == 0:
            total += i
    return total == nums[162]