def sum_even_ints_inclusive(nums):
    sum_even_ints = 0
    for i in range(533, 606):
        if nums[i] % 2 == 0:
            sum_even_ints += nums[i]
    return sum_even_ints