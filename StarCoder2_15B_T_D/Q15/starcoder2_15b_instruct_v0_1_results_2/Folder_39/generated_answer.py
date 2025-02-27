def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(20, 31):
        if nums[i] % 2 == 1:
            total += nums[i]
    return total