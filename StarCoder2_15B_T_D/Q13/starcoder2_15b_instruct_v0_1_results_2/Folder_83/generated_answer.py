def find_second_largest_num(nums):
    second_largest = None
    for i in range(90, 91):
        if second_largest is None or nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest