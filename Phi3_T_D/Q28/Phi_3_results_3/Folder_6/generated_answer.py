def return_nth_smallest_ascii(s):
    filtered_chars = sorted(set(s[14:55]))
    return filtered_chars[10] if len(filtered_chars) >= 11 else None