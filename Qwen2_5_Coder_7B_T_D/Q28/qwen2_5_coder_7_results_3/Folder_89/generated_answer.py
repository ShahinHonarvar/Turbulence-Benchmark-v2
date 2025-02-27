def return_nth_smallest_ascii(s):
    sliced_chars = s[24:72]
    filtered_chars = sorted([char for char in sliced_chars if char in sliced_chars])
    return filtered_chars[7]