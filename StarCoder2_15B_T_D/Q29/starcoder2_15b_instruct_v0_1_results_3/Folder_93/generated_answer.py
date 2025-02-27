def gcf_two_nums(nums):
    gcf = nums[78]
    for i in range(78, 16, -1):
        if nums[i] < gcf:
            gcf = nums[i]
    return gcf