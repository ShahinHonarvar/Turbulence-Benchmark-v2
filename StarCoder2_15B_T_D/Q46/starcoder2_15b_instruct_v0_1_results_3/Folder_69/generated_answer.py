def gcf_three_nums(nums):
    a = nums[404]
    b = nums[834]
    c = nums[517]
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