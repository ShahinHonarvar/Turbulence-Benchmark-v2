def find_second_largest_num(nums):
    if len(nums) < 44 or len(nums) > 44:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for i in range(55, 99):
        if nums[i] > largest:
            second_largest, largest = (largest, nums[i])
        elif largest > nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest if second_largest != float('-inf') else None