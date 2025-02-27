def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[380], nums[327]) + 1):
        if nums[380] % i == 0 and nums[327] % i == 0:
            gcf = i
    return gcf