def gcf_three_nums(nums):
    gcf59 = nums[59]
    gcf93 = nums[93]
    gcf84 = nums[84]
    for i in range(min(gcf59, gcf93, gcf84), 1, -1):
        if gcf59 % i == 0 and gcf93 % i == 0 and (gcf84 % i == 0):
            return i