def gcf_two_nums(nums):
    if len(nums) < 2:
        return None
    if 85 >= len(nums) or 33 >= len(nums):
        return None
    gcf = nums[85]
    for i in range(86, len(nums)):
        if nums[i] < gcf:
            gcf = nums[i]
    return gcf