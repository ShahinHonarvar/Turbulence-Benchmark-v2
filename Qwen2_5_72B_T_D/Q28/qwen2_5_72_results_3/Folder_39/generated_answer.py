def return_nth_smallest_ascii(s):
    if len(s) < 67:
        return None
    substring = s[1:67]
    char_list = sorted(substring)
    if len(char_list) < 8:
        return None
    return char_list[7]