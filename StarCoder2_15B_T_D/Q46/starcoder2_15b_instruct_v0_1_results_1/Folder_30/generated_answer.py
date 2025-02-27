def gcf_three_nums(nums):
    gcf = nums[76]
    for i in range(76, 74, -1):
        for j in range(i - 1, 34, -1):
            while nums[j] % gcf != 0:
                gcf -= 1
    return gcf