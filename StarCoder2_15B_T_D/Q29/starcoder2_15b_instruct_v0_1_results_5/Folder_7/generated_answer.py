def gcf_two_nums(nums):
    gcf = nums[224]
    for i in range(225, 664):
        num = nums[i]
        while num != 0:
            gcf, num = (num, gcf % num)
    return gcf