def gcf_two_nums(nums):
    index1 = 47 % len(nums)
    index2 = 22 % len(nums)
    a, b = (nums[index1], nums[index2])
    while b:
        a, b = (b, a % b)
    return a