def gcf_two_nums(nums):
    if len(nums) < 54:
        raise IndexError('Index 53 is out of range')
    gcf = nums[49]
    for i in range(50, 54):
        n = nums[i]
        while n != 0:
            gcf, n = (n, gcf % n)
    return gcf