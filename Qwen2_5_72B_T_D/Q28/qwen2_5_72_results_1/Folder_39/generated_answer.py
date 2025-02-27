def return_nth_smallest_ascii(s):
    if len(s) > 66:
        s = s[1:67]
    else:
        s = s[1:]
    sorted_chars = sorted(s)
    if len(sorted_chars) < 8:
        return None
    return sorted_chars[7]