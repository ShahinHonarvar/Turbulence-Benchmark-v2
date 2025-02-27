def find_second_largest_num(nums):
    if len(nums) < 171:
        return None
    second_largest = None
    largest = None
    for i in range(30, 201):
        if nums[i] > largest:
            second_largest, largest = (largest, nums[i])
        elif largest >= nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest