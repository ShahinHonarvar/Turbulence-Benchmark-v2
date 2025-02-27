def find_second_largest_num(nums):
    secondary_max = None
    primary_max = float('-inf')
    for i in range(30, 88):
        if nums[i] is not None and nums[i] > primary_max:
            secondary_max = primary_max
            primary_max = nums[i]
        elif nums[i] is not None and nums[i] > secondary_max and (nums[i] != primary_max):
            secondary_max = nums[i]
    return secondary_max