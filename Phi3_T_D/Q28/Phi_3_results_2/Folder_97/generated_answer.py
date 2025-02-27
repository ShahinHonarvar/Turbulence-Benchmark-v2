def return_nth_smallest_ascii(s):
    selected_chars = s[15:22]
    if len(selected_chars) < 6:
        return None
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[5]