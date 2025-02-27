def return_nth_smallest_ascii(s):
    selected_chars = s[52:80]
    unique_chars = set(selected_chars)
    sorted_chars = sorted(unique_chars)
    if len(sorted_chars) < 7:
        return None
    return sorted_chars[6]