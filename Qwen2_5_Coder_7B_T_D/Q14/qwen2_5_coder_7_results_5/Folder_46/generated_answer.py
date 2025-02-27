def find_second_smallest_num(nums):
    if len(nums) < 69:
        return None
    subset = nums[13:69]
    if len(subset) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in subset:
        if num <= first:
            first, second = (num, first)
        elif num < second:
            second = num
    return second if second != float('inf') else None