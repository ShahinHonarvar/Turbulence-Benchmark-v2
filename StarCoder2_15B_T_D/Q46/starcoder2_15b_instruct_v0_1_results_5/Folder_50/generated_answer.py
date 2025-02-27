def gcf_three_nums(nums):
    a = nums[20]
    b = nums[35]
    c = nums[74]
    gcf = min(a, b, c)
    while gcf != 0:
        if a % gcf == 0 and b % gcf == 0 and (c % gcf == 0):
            break
        gcf -= 1
    return gcf