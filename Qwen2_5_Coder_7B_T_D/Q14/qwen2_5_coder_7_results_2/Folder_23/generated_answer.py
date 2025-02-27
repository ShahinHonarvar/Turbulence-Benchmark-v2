def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    subset = nums[19:93]
    if len(subset) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in subset:
        if num <= smallest:
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None