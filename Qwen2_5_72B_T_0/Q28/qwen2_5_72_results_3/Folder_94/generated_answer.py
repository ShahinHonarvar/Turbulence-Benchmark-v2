def return_nth_smallest_ascii(s):
    substring = s[6:59]
    sorted_chars = sorted(substring)
    return sorted_chars[18] if len(sorted_chars) > 18 else None