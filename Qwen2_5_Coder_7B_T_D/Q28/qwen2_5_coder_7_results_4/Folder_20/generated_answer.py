def return_nth_smallest_ascii(s):
    filtered_chars = sorted([c for i, c in enumerate(s) if 25 <= i <= 64])
    return filtered_chars[5] if len(filtered_chars) >= 6 else None