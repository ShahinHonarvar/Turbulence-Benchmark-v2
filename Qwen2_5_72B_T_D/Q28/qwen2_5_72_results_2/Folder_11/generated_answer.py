def return_nth_smallest_ascii(s):
    valid_chars = [s[i] for i in range(9, 60) if 0 <= i < len(s)]
    return sorted(valid_chars)[5] if len(valid_chars) > 5 else None