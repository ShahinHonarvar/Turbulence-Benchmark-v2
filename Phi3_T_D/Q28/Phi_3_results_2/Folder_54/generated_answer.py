def return_nth_smallest_ascii(s):
    filtered_chars = sorted(s[12:88])
    if len(filtered_chars) >= 17:
        return filtered_chars[16]
    return None