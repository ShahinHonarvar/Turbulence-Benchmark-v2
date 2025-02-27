def return_nth_smallest_ascii(s):
    target_chars = [s[i] for i in range(62, 84) if i < len(s)]
    target_chars.sort(key=ord)
    return target_chars[8] if len(target_chars) > 8 else None