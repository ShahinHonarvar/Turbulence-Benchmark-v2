def return_nth_smallest_ascii(s):
    valid_chars = [s[i] for i in range(1, 32) if i < len(s)]
    valid_chars_sorted = sorted(valid_chars)
    return valid_chars_sorted[5] if len(valid_chars_sorted) > 5 else None