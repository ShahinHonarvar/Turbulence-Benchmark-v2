def return_n_smallest_chars(s):
    combined_list = []
    for char in sorted(s):
        combined_list.extend([char] * 70)
    return combined_list