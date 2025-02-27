def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('The list must contain at least three elements.')
    if not all((isinstance(num, int) and num > 0 for num in nums)):
        raise ValueError('The list must contain only positive integers.')
    four_hundredth_element = nums[404]
    eight_hundred_and_thirty_fourth_element = nums[834]
    five_hundred_and_seventeenth_element = nums[517]
    gcf = four_hundredth_element
    for num in (eight_hundred_and_thirty_fourth_element, five_hundred_and_seventeenth_element):
        while num != 0:
            gcf, num = (num, gcf % num)
    return gcf