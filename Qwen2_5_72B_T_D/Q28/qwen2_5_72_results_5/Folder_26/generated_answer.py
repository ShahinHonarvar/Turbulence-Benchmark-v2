def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(1, 37) if i < len(s)]
    sorted_chars = sorted(chars)
    return sorted_chars[14] if len(sorted_chars) > 14 else None