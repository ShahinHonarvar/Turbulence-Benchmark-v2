def gcf_two_nums(nums):
    gcf = nums[87]
    for i in range(87, 95):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf