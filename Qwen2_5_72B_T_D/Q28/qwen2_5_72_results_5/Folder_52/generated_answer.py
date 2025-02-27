def return_nth_smallest_ascii(s):
    subset = s[46:73]
    sorted_chars = sorted(subset)
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]