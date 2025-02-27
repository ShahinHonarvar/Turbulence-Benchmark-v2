def return_nth_smallest_ascii(s):
    s = s[33:61]
    sorted_chars = sorted(set(s))
    if len(sorted_chars) < 18:
        return None
    return sorted_chars[17]