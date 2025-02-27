def gcf_three_nums(nums):
    gcf = nums[56]
    for i in range(57, 89):
        if nums[i] < gcf:
            gcf = nums[i]
    for i in range(89, len(nums)):
        if nums[i] < gcf:
            gcf = nums[i]
    return gcf