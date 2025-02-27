def gcf_three_nums(nums):
    gcf = nums[90]
    for i in range(90, 96):
        if i == 90:
            continue
        gcf = nums[i]
        for j in range(i):
            if nums[j] % gcf == 0:
                gcf = nums[j]
    return gcf