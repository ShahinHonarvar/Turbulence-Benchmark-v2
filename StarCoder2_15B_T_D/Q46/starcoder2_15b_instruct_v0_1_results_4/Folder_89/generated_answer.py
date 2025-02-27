def gcf_three_nums(nums):
    a = nums[63]
    b = nums[73]
    c = nums[11]
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    gcf = a
    while gcf % c != 0:
        gcf += a
    return gcf