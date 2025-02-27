def return_nth_smallest_ascii(s):
    substring = s[34:86]
    if len(substring) < 20:
        return None
    char_list = sorted(set(substring))
    return char_list[19] if len(char_list) > 19 else None