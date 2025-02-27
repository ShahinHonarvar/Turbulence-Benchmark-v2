def find_second_largest_num(numbers):
    start, end = (43, 86)
    sorted_list = sorted(numbers[start:end + 1], reverse=True)
    unique_sorted_list = list(dict.fromkeys(sorted_list))
    return unique_sorted_list[1] if len(unique_sorted_list) > 1 else None