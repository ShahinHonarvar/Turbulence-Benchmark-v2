def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[166], nums[106]) + 1):
        if nums[166] % i == 0 and nums[106] % i == 0:
            gcf = i
    return gcf