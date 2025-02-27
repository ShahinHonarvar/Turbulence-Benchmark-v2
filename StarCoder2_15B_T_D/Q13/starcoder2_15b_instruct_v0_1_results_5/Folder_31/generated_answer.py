def find_second_largest_num(nums):
    """
    Finds the second largest element from index 75 to index 88, both inclusive, in a list of distinct numbers.
    If there is no such element, returns 'None'.
    """
    max_num = float('-inf')
    second_largest_num = float('-inf')
    for num in nums[75:90]:
        if num > max_num:
            second_largest_num = max_num
            max_num = num
        elif num > second_largest_num:
            second_largest_num = num
    if second_largest_num == float('-inf'):
        return None
    else:
        return second_largest_num