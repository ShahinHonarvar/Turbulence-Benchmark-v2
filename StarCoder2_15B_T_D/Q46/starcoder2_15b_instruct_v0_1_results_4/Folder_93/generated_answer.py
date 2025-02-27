def gcf_three_nums(nums):
    a = nums[25]
    b = nums[76]
    c = nums[57]
    while b != 0:
        a, b = (b, a % b)
    gcd = a
    while c != 0:
        gcd, c = (c, gcd % c)
    return gcd