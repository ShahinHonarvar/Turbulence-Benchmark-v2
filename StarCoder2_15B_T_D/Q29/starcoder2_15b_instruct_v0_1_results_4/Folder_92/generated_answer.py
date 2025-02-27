def gcf_two_nums(nums):
    if len(nums) < 2:
        return None
    gcf = nums[0]
    for num in nums[1:]:
        while num != 0:
            gcf, num = (num, gcf % num)
    return gcf