def find_second_smallest_num(nums):
    if len(nums) < 101:
        return None
    sublist = nums[10:101]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            second = first
            first = num
        elif num < second:
            second = num
    return second if second != float('inf') else None