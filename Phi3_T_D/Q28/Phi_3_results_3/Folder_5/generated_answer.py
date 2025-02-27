def return_nth_smallest_ascii(s):
    char_set = sorted(set(s[5:90]))
    return char_set[12] if len(char_set) >= 13 else None