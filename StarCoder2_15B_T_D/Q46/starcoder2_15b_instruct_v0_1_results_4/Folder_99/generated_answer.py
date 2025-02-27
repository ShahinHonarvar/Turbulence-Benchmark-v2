def gcf_three_nums(nums):
    a = nums[912]
    b = nums[170]
    c = nums[500]
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    while b != c:
        if b > c:
            b -= c
        else:
            c -= b
    return a