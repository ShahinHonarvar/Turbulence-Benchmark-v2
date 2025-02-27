def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    sub_list = nums[12:93]
    if len(sub_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sub_list:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None