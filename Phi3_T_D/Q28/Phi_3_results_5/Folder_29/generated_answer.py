def return_nth_smallest_ascii(s):
    wanted_chars = sorted(s[5:11])
    return wanted_chars[5 - 1] if len(wanted_chars) >= 6 else None