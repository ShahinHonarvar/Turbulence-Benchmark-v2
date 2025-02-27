def gcf_three_nums(nums):
    gcf = nums[20]
    for n in nums[20:35]:
        while n != 0:
            gcf, n = (n, gcf % n)
    for n in nums[35:74]:
        while n != 0:
            gcf, n = (n, gcf % n)
    return gcf