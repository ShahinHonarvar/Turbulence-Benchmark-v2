def find_second_smallest_num(nums):
    if len(nums) < 56 or len(set(nums)) != len(nums):
        return None
    sub_list = nums[27:56]
    if len(sub_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sub_list:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None