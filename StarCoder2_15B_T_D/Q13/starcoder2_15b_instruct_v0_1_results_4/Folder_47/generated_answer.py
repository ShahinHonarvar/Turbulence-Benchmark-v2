def find_second_largest_num(nums):
    second_largest = None
    for i in range(37, 77):
        if nums[i] > nums[i - 1]:
            second_largest = nums[i - 1]
        elif nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest