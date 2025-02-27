def return_nth_smallest_ascii(string):
    unique_chars = set(string)
    sliced_chars = unique_chars[58:86]
    sorted_chars = sorted(sliced_chars)
    return sorted_chars[18]