def gcf_three_nums(nums):
    a, b, c = (nums[990], nums[671], nums[711])
    while b:
        a, b = (b, a % b)
    return a