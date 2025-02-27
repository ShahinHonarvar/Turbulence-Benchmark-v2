def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0 and 17 <= i <= 78:
            sum += nums[i]
    return sum