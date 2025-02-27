def gcf_two_nums(nums):
    a, b = (nums[87], nums[95])
    while b:
        a, b = (b, a % b)
    return a