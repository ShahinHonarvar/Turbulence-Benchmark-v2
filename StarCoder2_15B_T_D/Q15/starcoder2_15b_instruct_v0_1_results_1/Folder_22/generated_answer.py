def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(len(nums)):
        if i >= 40 and i <= 41 and (nums[i] % 2 != 0):
            total += nums[i]
    return total