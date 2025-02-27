def return_nth_smallest_ascii(s):
    chars = [c for c in s[46:73]]
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[14] if len(sorted_chars) > 14 else None