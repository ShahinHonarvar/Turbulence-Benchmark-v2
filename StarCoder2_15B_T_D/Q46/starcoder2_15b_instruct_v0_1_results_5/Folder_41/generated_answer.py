def gcf_three_nums(nums):
    gcf = nums[19]
    for num in nums[19 + 1:]:
        while num != 0:
            gcf, num = (num, gcf % num)
    return gcf