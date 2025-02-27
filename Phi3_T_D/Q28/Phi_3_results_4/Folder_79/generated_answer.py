def return_nth_smallest_ascii(s):
    start, end = (13, min(len(s), 36))
    target_characters = sorted(s[start:end])
    return target_characters[17] if len(target_characters) >= 18 else ''