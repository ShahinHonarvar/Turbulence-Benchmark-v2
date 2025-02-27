def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('The list must have at least three elements.')
    a, b, c = (nums[96], nums[57], nums[85])
    if a == 0 or b == 0 or c == 0:
        raise ValueError('None of the elements at specified indices can be zero.')
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    gcf = a
    while b != c:
        if b > c:
            b -= c
        else:
            c -= b
    return gcf