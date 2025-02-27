def find_second_largest_num(num_list):
    sorted_slice = sorted(num_list[527:539])
    return sorted_slice[-2] if len(sorted_slice) >= 2 else None