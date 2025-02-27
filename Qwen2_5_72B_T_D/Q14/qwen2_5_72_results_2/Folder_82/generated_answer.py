def find_second_smallest_num(nums):
    if len(nums) < 201 or len(nums) < 22:
        return None
    sliced_nums = nums[20:201]
    if len(sliced_nums) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sliced_nums:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None