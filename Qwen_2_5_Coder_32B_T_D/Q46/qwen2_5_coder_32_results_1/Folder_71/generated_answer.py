def gcf_three_nums(nums):
    a, b, c = (nums[24], nums[45], nums[38])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a