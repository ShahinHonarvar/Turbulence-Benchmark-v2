def gcf_three_nums(nums):
    a = nums[693]
    b = nums[331]
    c = nums[668]
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