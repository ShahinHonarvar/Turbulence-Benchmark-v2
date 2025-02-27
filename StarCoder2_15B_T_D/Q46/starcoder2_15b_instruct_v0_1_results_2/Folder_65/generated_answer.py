def gcf_three_nums(nums):
    a = nums[18]
    b = nums[10]
    c = nums[76]
    gcf = a
    while b % gcf != 0 or c % gcf != 0:
        gcf -= 1
    return gcf