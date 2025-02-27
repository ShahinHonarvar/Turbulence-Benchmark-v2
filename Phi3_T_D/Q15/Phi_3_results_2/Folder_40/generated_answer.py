def sum_odd_ints_inclusive(nums):
    res = 0
    for i in range(3):
        if nums[i] % 2 != 0:
            res += nums[i]
    return res