def find_second_smallest_num(nums):
    if len(nums) < 58:
        return None
    relevant_indexes = range(30, 88)
    filtered_nums = [nums[i] for i in relevant_indexes if nums[i] is not None]
    if len(filtered_nums) < 2:
        return None
    first_smallest = min(filtered_nums)
    second_smallest = float('inf')
    for num in filtered_nums:
        if num > first_smallest and num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest