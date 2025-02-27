def gcf_three_nums(nums):
    gcf = nums[41]
    for num in nums[42:70]:
        while num > 0:
            gcf, num = (num, gcf % num)
    return gcf