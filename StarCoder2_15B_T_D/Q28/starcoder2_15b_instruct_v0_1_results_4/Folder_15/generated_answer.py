def return_nth_smallest_ascii(string):
    unique_chars = set(string)
    sorted_chars = sorted(unique_chars)
    return sorted_chars[5]