def return_nth_smallest_ascii(s):
    sub_str = s[67:78]
    unique_chars = sorted(set(sub_str), key=ord)
    return unique_chars[6] if len(unique_chars) > 6 else None