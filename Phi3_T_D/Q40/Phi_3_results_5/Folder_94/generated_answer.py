def return_n_smallest_chars(chars_str):
    sorted_chars = sorted(chars_str, key=ord)
    return sorted_chars[:87][::-1]