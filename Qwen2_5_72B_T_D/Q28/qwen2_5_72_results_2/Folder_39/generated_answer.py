def return_nth_smallest_ascii(s):
    valid_chars = s[1:67]
    sorted_chars = sorted(valid_chars)
    return sorted_chars[7]