def sum_even_ints_inclusive(nums):
    if len(nums) < 49:
        return 0
    sum_even = 0
    for i in range(30, 49):
        if nums[i] % 2 == 0:
            sum_even += nums[i]
    return sum_even