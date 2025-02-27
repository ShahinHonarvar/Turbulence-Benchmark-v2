def gcf_two_nums(nums):
    if len(nums) < 722:
        return -1
    gcf = nums[360]
    for i in range(361, 723):
        if nums[i] < gcf:
            gcf = nums[i]
    return gcf