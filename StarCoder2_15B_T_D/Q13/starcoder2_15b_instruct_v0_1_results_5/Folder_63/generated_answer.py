def find_second_largest_num(nums):
    second_largest = None
    for i in range(22, 89):
        if nums[i] > nums[i - 1]:
            second_largest = nums[i - 1]
    return second_largest