def return_nth_smallest_ascii(s):
    s = s[10:91]
    sorted_chars = sorted(s)
    if len(sorted_chars) >= 20:
        return sorted_chars[19]
    return None