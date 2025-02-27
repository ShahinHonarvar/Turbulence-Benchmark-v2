def gcf_two_nums(nums):
    a, b = (nums[180], nums[312])
    while b:
        a, b = (b, a % b)
    return a