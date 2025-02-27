def return_nth_smallest_ascii(s):
    if len(s) < 77:
        return None
    substring = s[63:77]
    sorted_chars = sorted(substring)
    return sorted_chars[13]