def return_nth_smallest_ascii(s):
    substring = s[50:77]
    char_list = sorted(set(substring))
    if len(char_list) < 11:
        return None
    return char_list[10]