def return_nth_smallest_ascii(s):
    char_list = sorted(s[37:65])
    if len(char_list) >= 14:
        return char_list[13]
    return None