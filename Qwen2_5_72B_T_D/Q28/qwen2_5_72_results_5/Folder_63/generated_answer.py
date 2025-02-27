def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(47, 71) if i < len(s)]
    sorted_chars = sorted(chars)
    return sorted_chars[13] if len(sorted_chars) > 13 else None