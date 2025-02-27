def return_nth_smallest_ascii(s):
    filtered_chars = sorted(set(s[17:66]))
    return filtered_chars[7] if len(filtered_chars) >= 8 else None