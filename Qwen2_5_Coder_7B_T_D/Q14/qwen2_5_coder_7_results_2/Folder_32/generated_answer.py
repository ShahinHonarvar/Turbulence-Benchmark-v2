def find_second_smallest_num(nums):
    if len(nums) < 36:
        return None
    subset = nums[32:36]
    if len(subset) < 2:
        return None
    smallest = min(subset[0], subset[1])
    second_smallest = max(subset[0], subset[1])
    for num in subset[2:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != smallest else None