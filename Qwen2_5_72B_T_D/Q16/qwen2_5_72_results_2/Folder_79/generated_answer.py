def sum_even_ints_inclusive(nums):
    if 4 < len(nums):
        if nums[4] % 2 == 0:
            return nums[4]
        else:
            return 0
    else:
        return 0