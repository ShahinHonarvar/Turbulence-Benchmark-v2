def find_second_largest_num(num_list):
    start, end = (246, min(750, len(num_list)))
    unique_sorted = sorted(set(num_list[start:end + 1]), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None