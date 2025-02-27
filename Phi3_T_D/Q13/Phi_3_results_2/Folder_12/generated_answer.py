def find_second_largest_num(nums):
    second_largest = None
    for i in range(14, 65):
        if second_largest is None or nums[i] > second_largest:
            second_largest, largest = (nums[i], second_largest)
        elif largest > nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest