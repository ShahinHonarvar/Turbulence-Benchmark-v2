def return_nth_smallest_ascii(s):
    if not s or len(s) <= 87 - 12 + 1:
        return ''
    target_slice = s[12:88]
    unique_chars = sorted(set(target_slice), key=ord)
    if len(unique_chars) < 17:
        return ''
    return unique_chars[16]