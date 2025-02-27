def return_nth_smallest_ascii(s):
    target_range = s[18:46]
    unique_chars = set(target_range)
    return sorted(unique_chars, key=ord)[6]