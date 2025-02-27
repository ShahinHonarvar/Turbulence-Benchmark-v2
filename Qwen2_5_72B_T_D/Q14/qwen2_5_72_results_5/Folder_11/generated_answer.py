def find_second_smallest_num(nums):
    if not 93 <= len(nums) >= 66:
        return None
    selected_nums = nums[66:94]
    if len(selected_nums) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in selected_nums:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None