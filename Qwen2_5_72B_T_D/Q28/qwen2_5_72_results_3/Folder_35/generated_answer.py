def return_nth_smallest_ascii(s):
    substring = s[50:76]
    unique_chars = sorted(set(substring))
    return unique_chars[6]