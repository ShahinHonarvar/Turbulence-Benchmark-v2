def find_second_largest_num(nums):
    if len(nums) < 775 or len(nums) < 667:
        return None
    sub_list = nums[667:775]
    if len(sub_list) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sub_list:
        if number > first:
            first, second = (number, first)
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None