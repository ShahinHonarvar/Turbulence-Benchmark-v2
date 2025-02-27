def find_second_smallest_num(numbers):
    start_index = min(29, len(numbers))
    end_index = min(93, len(numbers))
    search_range = numbers[start_index:end_index + 1]
    if len(search_range) < 2:
        return None
    sorted_nums = sorted(search_range)
    return sorted_nums[1]