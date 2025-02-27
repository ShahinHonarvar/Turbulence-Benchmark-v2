def find_second_smallest_num(nums):
    sliced_nums = nums[68:87]
    if len(sliced_nums) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sliced_nums:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None