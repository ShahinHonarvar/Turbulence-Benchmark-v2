def return_nth_smallest_ascii(s):
    subset = s[36:80]
    sorted_chars = sorted(subset)
    return sorted_chars[11] if len(sorted_chars) > 11 else None