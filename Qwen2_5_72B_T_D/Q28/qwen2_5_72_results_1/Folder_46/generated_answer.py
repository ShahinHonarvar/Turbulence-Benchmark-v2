def return_nth_smallest_ascii(s):
    substring = s[34:86]
    filtered_chars = sorted(substring)
    return filtered_chars[19]