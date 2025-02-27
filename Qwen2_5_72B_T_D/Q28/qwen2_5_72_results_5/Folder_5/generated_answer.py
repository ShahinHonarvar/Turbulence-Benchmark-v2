def return_nth_smallest_ascii(s):
    subset = s[5:90]
    char_list = sorted(list(subset))
    return char_list[12] if len(char_list) > 12 else None