def gcf_two_nums(nums):
    a, b = (nums[894], nums[801])
    while b:
        a, b = (b, a % b)
    return a