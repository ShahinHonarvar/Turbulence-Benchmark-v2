def find_second_largest_num(numbers):
    start, end = (42, 68)
    sliced_list = numbers[start:end + 1]
    sorted_list = sorted(sliced_list, reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else None