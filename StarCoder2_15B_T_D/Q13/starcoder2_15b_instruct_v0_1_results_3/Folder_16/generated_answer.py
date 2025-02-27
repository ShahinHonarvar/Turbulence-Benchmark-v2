def find_second_largest_num(nums):
    second_largest = None
    for i in range(33, 37):
        if nums[i] > second_largest or second_largest is None:
            second_largest = nums[i]
    return second_largest