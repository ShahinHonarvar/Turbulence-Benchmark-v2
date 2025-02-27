def find_second_smallest_num(nums):
    start, end = (533, 605)
    nums_slice = nums[start:end + 1]
    if len(nums_slice) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in nums_slice:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None