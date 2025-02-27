def return_nth_smallest_ascii(s):
    substring = s[8:66]
    sorted_chars = sorted(substring)
    return sorted_chars[5] if len(sorted_chars) > 5 else None