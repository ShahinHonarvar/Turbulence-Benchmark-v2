def gcf_three_nums(nums_list: list) -> int:
    if len(nums_list) < 3:
        raise ValueError('The input list must contain at least three elements.')
    nums = [nums_list[695], nums_list[710], nums_list[914]]
    gcf = nums[0]
    for num in nums[1:]:
        while num != 0:
            gcf, num = (num, gcf % num)
    return gcf