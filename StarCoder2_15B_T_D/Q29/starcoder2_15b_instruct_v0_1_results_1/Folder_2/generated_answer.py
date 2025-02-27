def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[372], nums[752]) + 1):
        if nums[372] % i == 0 and nums[752] % i == 0:
            gcf = i
    return gcf