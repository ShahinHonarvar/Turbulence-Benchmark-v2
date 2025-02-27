def find_second_largest_num(nums):
    max_num = float('-inf')
    max_index = None
    for i, num in enumerate(nums):
        if num > max_num:
            max_num = num
            max_index = i
    second_largest_num = float('-inf')
    for i, num in enumerate(nums):
        if i != max_index and num > second_largest_num:
            second_largest_num = num
    return second_largest_num