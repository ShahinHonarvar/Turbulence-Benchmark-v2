def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(38, 83) if i < len(s)]
    sorted_chars = sorted(chars)
    return sorted_chars[19] if len(sorted_chars) > 19 else None