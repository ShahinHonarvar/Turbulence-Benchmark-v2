def return_nth_smallest_ascii(s):
    filtered_chars = sorted(s[5:83])
    return filtered_chars[15] if len(filtered_chars) >= 16 else None