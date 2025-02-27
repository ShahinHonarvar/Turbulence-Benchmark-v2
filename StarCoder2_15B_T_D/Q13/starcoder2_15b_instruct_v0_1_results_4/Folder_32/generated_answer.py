def find_second_largest_num(nums):
    if len(nums) < 22:
        return None
    second_largest = nums[21]
    for i in range(22, 98):
        if nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest