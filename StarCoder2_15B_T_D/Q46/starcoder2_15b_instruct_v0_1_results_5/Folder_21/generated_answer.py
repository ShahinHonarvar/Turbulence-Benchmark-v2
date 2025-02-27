def gcf_three_nums(nums):
    a = nums[412]
    b = nums[932]
    c = nums[337]
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