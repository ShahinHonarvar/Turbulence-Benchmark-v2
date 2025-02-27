def return_nth_smallest_ascii(s):
    char_list = sorted(s[20:31])
    return char_list[7] if len(char_list) >= 8 else None