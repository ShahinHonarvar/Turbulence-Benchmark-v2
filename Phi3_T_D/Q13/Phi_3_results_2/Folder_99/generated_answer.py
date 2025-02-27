def find_second_largest_num(nums):
    start_index, end_index = (310, 370)
    nums_slice = nums[start_index:end_index + 1]
    if len(nums_slice) < 2:
        return None
    max_num = max(nums_slice)
    nums_slice.remove(max_num)
    second_max_num = max(nums_slice)
    return second_max_num