def find_second_largest_num(nums):
    range_start = max(533, min(len(nums), 605))
    if range_start >= len(nums):
        return None
    largest = second_largest = float('-inf')
    for i in range(range_start, min(range_start + 73, len(nums))):
        if nums[i] > largest:
            second_largest, largest = (largest, nums[i])
        elif largest > nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest if second_largest != float('-inf') else None