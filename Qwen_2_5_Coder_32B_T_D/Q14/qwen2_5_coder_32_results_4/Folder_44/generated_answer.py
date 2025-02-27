def find_second_smallest_num(nums):
    if len(nums) < 100:
        return None
    sub_list = nums[91:100]
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