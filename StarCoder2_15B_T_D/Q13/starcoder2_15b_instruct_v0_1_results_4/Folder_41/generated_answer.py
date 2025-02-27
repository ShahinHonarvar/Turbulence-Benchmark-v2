def find_second_largest_num(nums):
    second_largest = None
    for i in range(6, len(nums)):
        if nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest