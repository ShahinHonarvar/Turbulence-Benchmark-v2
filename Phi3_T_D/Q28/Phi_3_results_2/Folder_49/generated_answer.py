def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[20:81]))
    if len(unique_chars) >= 11:
        return unique_chars[10]
    else:
        return None