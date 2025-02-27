def find_second_largest_num(nums):
    largest = max(nums[1:6])
    second_largest = None
    for i in range(1, 6):
        if nums[i] < largest and (second_largest is None or nums[i] > second_largest):
            second_largest = nums[i]
    return second_largest