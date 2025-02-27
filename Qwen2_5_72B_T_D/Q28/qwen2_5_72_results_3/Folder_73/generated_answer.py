def return_nth_smallest_ascii(s):
    if len(s) < 70:
        filtered_chars = s[:70]
    else:
        filtered_chars = s
    sorted_chars = sorted(filtered_chars)
    if len(sorted_chars) < 10:
        return None
    return sorted_chars[9]