def return_nth_smallest_ascii(s):
    chars = s[50:77]
    sorted_chars = sorted(chars)
    return sorted_chars[10] if len(sorted_chars) > 10 else None