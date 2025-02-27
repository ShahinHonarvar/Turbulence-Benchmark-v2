def return_nth_smallest_ascii(s):
    target_chars = sorted(s[16:86 + 1])[:15]
    return target_chars[-1] if target_chars else None