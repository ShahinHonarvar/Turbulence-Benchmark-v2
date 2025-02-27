def return_nth_smallest_ascii(s):
    if len(s) < 67:
        return None
    substring = s[1:67]
    sorted_chars = sorted(substring)
    return sorted_chars[7]