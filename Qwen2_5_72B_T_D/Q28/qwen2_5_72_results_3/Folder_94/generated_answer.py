def return_nth_smallest_ascii(s):
    subset = s[6:59]
    sorted_chars = sorted(subset)
    if len(sorted_chars) < 19:
        return None
    return sorted_chars[18]