def gcf_three_nums(nums):
    gcf = nums[87]
    for i in range(86, 19, -1):
        if nums[i] < gcf:
            gcf = nums[i]
    return gcf