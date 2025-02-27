def find_second_smallest_num(nums):
    if len(nums[19:93]) < 2:
        return None
    sub_nums = nums[19:93]
    first, second = (float('inf'), float('inf'))
    for num in sub_nums:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None