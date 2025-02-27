def return_nth_smallest_ascii(s):
    substring = s[25:89]
    filtered_chars = sorted(substring)
    return filtered_chars[10]