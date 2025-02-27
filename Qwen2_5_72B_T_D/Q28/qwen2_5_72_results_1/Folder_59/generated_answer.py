def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(12, len(s)))]
    chars_sorted = sorted(chars)
    if len(chars_sorted) < 12:
        return None
    return chars_sorted[11]