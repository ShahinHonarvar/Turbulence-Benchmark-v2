def return_nth_smallest_ascii(s):
    filtered_chars = s[29:34]
    return sorted(filtered_chars, key=ord)[4]