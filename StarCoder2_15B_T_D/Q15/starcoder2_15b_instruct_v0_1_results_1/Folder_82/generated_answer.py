def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(20, 201):
        if nums[i] % 2 == 1:
            sum += nums[i]
    return sum