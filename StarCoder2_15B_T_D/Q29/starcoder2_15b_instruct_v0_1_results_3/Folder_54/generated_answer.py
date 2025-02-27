def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[56], nums[92]) + 1):
        if nums[56] % i == 0 and nums[92] % i == 0:
            gcf = i
    return gcf