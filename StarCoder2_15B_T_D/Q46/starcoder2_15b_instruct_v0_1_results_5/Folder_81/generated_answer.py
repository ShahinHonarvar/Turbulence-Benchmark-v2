def gcf_three_nums(nums):
    num_20 = nums[20]
    num_17 = nums[17]
    num_28 = nums[28]
    gcf = min(num_20, num_17, num_28)
    while not (num_20 % gcf == 0 and num_17 % gcf == 0 and (num_28 % gcf == 0)):
        gcf -= 1
    return gcf