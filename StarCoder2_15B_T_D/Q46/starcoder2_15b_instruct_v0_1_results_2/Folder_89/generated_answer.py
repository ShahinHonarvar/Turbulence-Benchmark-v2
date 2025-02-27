def gcf_three_nums(nums):
    gcf = 1
    for i in [63, 73, 11]:
        for j in range(1, nums[i] + 1):
            if nums[i] % j == 0:
                gcf = j
    return gcf