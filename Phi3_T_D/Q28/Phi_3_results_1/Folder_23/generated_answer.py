def return_nth_smallest_ascii(chars):
    sub_chars = chars[29:48]
    sorted_chars = sorted(sub_chars, key=ord)
    return sorted_chars[6] if len(sorted_chars) >= 7 else ''