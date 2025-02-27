def find_second_smallest_num(nums):
    if len(nums) < 20 or max((i for i in range(52, 72) if i < len(nums))) - 52 < 2:
        return None
    start, end = (52, min(71, len(nums)))
    first, second = (float('inf'), float('inf'))
    for i in range(start, end + 1):
        if nums[i] < first:
            second = first
            first = nums[i]
        elif first < nums[i] < second:
            second = nums[i]
    return second if second != float('inf') else None