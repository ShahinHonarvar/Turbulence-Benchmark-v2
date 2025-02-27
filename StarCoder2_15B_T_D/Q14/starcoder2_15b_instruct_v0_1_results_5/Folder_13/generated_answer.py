def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(28, 33):
        if nums[i] < nums[28]:
            second_smallest = nums[28]
            nums[28] = nums[i]
        elif nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest