def return_nth_smallest_ascii(s):
    selected_chars = sorted(set(s[3:53]))
    return selected_chars[7] if len(selected_chars) > 7 else None