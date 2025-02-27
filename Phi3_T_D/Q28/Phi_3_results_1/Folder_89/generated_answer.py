def return_nth_smallest_ascii(s):
    selected_chars = sorted(s[24:72])
    return selected_chars[7] if len(selected_chars) > 7 else None