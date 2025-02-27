def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[47], nums[10]) + 1):
        if nums[47] % i == 0 and nums[10] % i == 0:
            gcf = i
    return gcf