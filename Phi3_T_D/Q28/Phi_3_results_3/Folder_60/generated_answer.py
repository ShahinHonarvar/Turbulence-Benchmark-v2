def return_nth_smallest_ascii(s):
    selected_chars = sorted(s[35:80])
    return selected_chars[11] if len(selected_chars) >= 12 else None