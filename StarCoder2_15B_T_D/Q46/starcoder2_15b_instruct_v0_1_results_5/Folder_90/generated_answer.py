def gcf_three_nums(nums):
    gcf = nums[818]
    for i in range(819, 874):
        if nums[i] < gcf:
            continue
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf