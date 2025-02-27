def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    second_largest = None
    for i in range(533, 606):
        if nums[i] > nums[i - 1]:
            second_largest = nums[i - 1]
    return second_largest