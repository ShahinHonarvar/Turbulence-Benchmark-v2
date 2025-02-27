def return_nth_smallest_ascii(s):
    selected_chars = s[25:78]
    if len(selected_chars) < 16:
        return None
    ascii_values = sorted(selected_chars)
    return ascii_values[15]