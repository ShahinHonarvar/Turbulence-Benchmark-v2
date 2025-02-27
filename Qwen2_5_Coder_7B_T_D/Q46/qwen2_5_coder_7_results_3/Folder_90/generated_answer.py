def gcf_three_nums(nums):
    a = nums[818]
    b = nums[606]
    c = nums[873]
    while b != 0:
        a, b = (b, a % b)
    return a