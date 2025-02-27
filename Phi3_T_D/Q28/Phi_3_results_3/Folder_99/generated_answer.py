def return_nth_smallest_ascii(s):
    sub_s = s[16:66]
    unique_chars = sorted(set(sub_s))
    return unique_chars[7] if len(unique_chars) >= 8 else None