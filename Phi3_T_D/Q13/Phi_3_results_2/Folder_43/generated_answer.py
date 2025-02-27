def find_second_largest_num(nums):
    if len(nums) < 86 - 68 + 1:
        return None
    second_largest = float('-inf')
    highest = float('-inf')
    for i in range(68, 87):
        if nums[i] > highest:
            second_largest, highest = (highest, nums[i])
        elif highest > nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest if second_largest != float('-inf') else None