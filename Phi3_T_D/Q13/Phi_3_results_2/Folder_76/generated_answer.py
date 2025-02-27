def find_second_largest_num(nums):
    selected_nums = nums[686:988]
    if len(selected_nums) < 2:
        return None
    first_largest, second_largest = (float('-inf'), float('-inf'))
    for num in selected_nums:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif first_largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None