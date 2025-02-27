def gcf_three_nums(nums):
    a = nums[912]
    b = nums[170]
    c = nums[500]
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