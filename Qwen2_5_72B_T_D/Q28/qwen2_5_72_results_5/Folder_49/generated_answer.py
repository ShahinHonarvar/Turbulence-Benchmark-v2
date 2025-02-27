def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(20, 81) if i < len(s)]
    chars_sorted = sorted(chars)
    return chars_sorted[10] if len(chars_sorted) > 10 else None