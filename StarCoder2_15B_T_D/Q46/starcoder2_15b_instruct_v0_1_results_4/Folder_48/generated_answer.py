def gcf_three_nums(nums):
    a = nums[654]
    b = nums[312]
    c = nums[441]
    gcd = a
    while b != 0:
        gcd = b
        b = a % b
    while c != 0:
        gcd = c
        c = gcd % c
    return gcd