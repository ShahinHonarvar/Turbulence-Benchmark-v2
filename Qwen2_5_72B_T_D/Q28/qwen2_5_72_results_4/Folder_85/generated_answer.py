def return_nth_smallest_ascii(s):
    substring = s[17:87]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 15:
        return sorted_chars[14]
    return None