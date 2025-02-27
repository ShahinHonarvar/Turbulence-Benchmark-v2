def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    first, second = (float('inf'), float('inf'))
    for num in nums[:8]:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None