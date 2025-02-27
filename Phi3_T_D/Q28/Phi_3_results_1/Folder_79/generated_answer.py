def return_nth_smallest_ascii(s):
    filtered_chars = sorted(set(s[12:36]))
    return filtered_chars[17] if len(filtered_chars) > 17 else None