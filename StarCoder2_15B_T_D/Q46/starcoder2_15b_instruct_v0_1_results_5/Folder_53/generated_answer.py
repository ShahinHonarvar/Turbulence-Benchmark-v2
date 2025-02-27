def gcf_three_nums(nums):
    n66 = nums[66]
    n56 = nums[56]
    n92 = nums[92]
    gcf = n66
    if n56 < gcf:
        gcf = n56
    if n92 < gcf:
        gcf = n92
    return gcf