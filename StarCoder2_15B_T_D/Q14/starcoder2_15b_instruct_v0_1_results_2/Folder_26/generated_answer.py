def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(62, 79):
        if nums[i] < nums[62]:
            second_smallest = nums[62]
            nums[62] = nums[i]
        elif nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest