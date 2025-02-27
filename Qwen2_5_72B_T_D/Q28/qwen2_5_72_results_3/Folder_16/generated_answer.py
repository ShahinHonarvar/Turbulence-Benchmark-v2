def return_nth_smallest_ascii(s):
    substring = s[18:46]
    chars = sorted(substring)
    return chars[6] if len(chars) > 6 else None