def find_second_largest_num(nums):
    start_index, end_index = (26, 52)
    sliced_list = nums[start_index:end_index + 1]
    if len(sliced_list) < 2:
        return None
    largest = max(sliced_list)
    sliced_list.remove(largest)
    return max(sliced_list)