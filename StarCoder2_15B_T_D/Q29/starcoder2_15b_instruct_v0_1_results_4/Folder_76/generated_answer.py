def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[184], nums[307]) + 1):
        if nums[184] % i == 0 and nums[307] % i == 0:
            gcf = i
    return gcf