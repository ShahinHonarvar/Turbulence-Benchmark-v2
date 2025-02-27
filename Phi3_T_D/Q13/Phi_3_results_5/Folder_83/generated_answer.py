def find_second_largest_num(nums):
    if not 90 <= len(nums) <= 91:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for i in range(90, 91):
        if nums[i] > largest:
            second_largest, largest = (largest, nums[i])
        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]
    return second_largest if second_largest != float('-inf') else None