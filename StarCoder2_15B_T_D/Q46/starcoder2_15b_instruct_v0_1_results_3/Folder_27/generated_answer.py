def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('List must have at least three elements')
    gcf = nums[76]
    for i in [64, 28]:
        while nums[i] % gcf != 0:
            gcf = nums[i] % gcf
    return gcf