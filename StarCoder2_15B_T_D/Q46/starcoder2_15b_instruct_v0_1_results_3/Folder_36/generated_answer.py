def gcf_three_nums(nums):
    a = nums[427]
    b = nums[761]
    c = nums[148]
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