def gcf_three_nums(nums):
    a = nums[70]
    b = nums[98]
    c = nums[22]
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    gcf = a
    while gcf % c != 0:
        gcf += a
    return gcf