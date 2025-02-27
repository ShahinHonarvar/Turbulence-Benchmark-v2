def find_second_largest_num(nums):
    if len(nums) < 201 or max(80, 200) > len(nums) - 1:
        return None
    sub_list = nums[80:201]
    if len(sub_list) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_list:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None