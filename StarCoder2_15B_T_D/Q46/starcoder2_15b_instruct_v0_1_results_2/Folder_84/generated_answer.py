def gcf_three_nums(nums):
    a = nums[695]
    b = nums[710]
    c = nums[914]
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