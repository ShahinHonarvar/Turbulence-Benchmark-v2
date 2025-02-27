def gcf_three_nums(nums):
    a = nums[427]
    b = nums[761]
    c = nums[148]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a