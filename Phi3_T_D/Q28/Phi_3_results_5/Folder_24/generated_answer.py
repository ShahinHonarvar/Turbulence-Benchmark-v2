def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[34:82]]
    unique_sorted_chars = sorted(set(filtered_chars), key=ord)
    return unique_sorted_chars[11]