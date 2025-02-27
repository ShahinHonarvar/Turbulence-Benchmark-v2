def gcf_three_nums(nums):
    a = nums[70]
    b = nums[98]
    c = nums[22]
    if a == 0:
        return b
    if b == 0:
        return a
    if c == 0:
        return a
    while b != c:
        if b > c:
            b -= c
        else:
            c -= b
    return b