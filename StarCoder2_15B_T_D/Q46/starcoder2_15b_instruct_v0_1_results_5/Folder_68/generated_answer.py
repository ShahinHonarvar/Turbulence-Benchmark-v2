def gcf_three_nums(nums):
    a = nums[4]
    b = nums[1]
    c = nums[7]
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    gcf = a
    while gcf != c:
        if gcf > c:
            gcf -= c
        else:
            c -= gcf
    return gcf