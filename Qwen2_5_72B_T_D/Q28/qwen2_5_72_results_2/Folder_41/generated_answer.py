def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 58 <= i <= 85]
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[18] if len(sorted_chars) > 18 else None