def return_nth_smallest_ascii(s):
    if len(s) < 70:
        s = s[:70]
    filtered_chars = sorted(set(s))
    if len(filtered_chars) >= 10:
        return filtered_chars[9]
    else:
        return None