def return_nth_smallest_ascii(s):
    selection = s[46:83]
    unique_selected = set(selection)
    sorted_chars = sorted(unique_selected, key=ord)
    return sorted_chars[15] if len(sorted_chars) > 15 else None