def gcf_three_nums(nums):
    gcf = nums[4]
    for num in nums[1:4] + nums[5:]:
        while num != 0:
            gcf, num = (num, gcf % num)
    return gcf