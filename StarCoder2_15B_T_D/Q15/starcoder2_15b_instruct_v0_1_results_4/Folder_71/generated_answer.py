def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(26, 53):
        if nums[i] % 2 == 1:
            sum_odd += nums[i]
    return sum_odd