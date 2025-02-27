def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('List must have at least three elements')
    gcf = nums[7]
    for num in nums[7:9]:
        while num > 0:
            gcf, num = (num, gcf % num)
    return gcf