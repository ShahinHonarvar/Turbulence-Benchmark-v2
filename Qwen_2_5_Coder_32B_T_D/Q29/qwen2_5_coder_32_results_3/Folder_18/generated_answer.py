def gcf_two_nums(nums):
    a, b = (nums[872], nums[219])
    while b:
        a, b = (b, a % b)
    return a