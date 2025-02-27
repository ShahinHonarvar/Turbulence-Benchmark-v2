def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[60:89]]
    sorted_filtered_chars = sorted(filtered_chars)
    nth_smallest_ascii = sorted_filtered_chars[6]
    return nth_smallest_ascii