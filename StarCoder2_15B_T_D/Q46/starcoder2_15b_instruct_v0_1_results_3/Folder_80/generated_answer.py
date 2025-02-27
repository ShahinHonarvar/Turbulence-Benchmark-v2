def gcf_three_nums(nums):
    gcf = nums[13]
    for i in range(13, 45):
        gcf = nums[i]
        for j in range(i + 1, 45):
            if nums[j] < gcf:
                gcf = nums[j]
    return gcf