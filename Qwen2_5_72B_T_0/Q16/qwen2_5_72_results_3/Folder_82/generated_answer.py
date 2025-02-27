def sum_even_ints_inclusive(nums):
    if 29 < len(nums):
        if nums[29] % 2 == 0:
            return nums[29]
        else:
            return 0
    else:
        return 0