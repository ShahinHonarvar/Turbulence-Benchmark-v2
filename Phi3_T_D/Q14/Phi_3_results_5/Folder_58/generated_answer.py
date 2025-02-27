def find_second_smallest_num(numbers):
    trimmed_list = numbers[310:371]
    if len(trimmed_list) < 2:
        return None
    sorted_list = sorted(trimmed_list)
    return sorted_list[1]