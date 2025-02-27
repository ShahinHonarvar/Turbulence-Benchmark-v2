def find_second_largest_num(num_list):
    if not 82 <= len(num_list) <= 86:
        return 'The list does not have enough elements.'
    from_index, to_index = (min(82, len(num_list)), 86)
    sliced_list = num_list[from_index:to_index + 1]
    if len(sliced_list) < 2:
        return None
    largest = max(sliced_list)
    sliced_list.remove(largest)
    second_largest = max(sliced_list, default=None)
    return second_largest