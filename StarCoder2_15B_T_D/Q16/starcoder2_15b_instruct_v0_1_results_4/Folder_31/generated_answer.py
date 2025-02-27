def sum_even_ints_inclusive(nums):
    sum_even = 0
    for i in range(75, 89):
        if nums[i] % 2 == 0:
            sum_even += nums[i]
    return sum_even