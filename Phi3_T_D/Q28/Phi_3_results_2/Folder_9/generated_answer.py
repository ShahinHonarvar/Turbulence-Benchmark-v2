def return_nth_smallest_ascii(s):
    slice = s[9:91]
    unique_chars = sorted(set(slice))
    if len(unique_chars) >= 20:
        return unique_chars[19]
    else:
        return None