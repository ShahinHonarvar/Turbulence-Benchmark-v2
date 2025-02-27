def return_nth_smallest_ascii(s):
    selected_chars = sorted(s[60:89])
    return selected_chars[6] if len(selected_chars) > 6 else None