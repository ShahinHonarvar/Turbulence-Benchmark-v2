def gcf_three_nums(nums):
    gcf = 1
    for i in [9, 6, 2]:
        for j in range(1, nums[i] + 1):
            if nums[i] % j == 0:
                gcf = j
    return gcf