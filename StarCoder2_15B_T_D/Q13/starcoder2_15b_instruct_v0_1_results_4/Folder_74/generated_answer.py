def find_second_largest_num(nums):
    second_largest = None
    for i in range(17, 79):
        if nums[i] > nums[i - 1]:
            second_largest = nums[i - 1]
    return second_largest