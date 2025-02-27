def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(len(nums)):
        if i >= 27 and i <= 55 and (nums[i] % 2 != 0):
            total += nums[i]
    return total