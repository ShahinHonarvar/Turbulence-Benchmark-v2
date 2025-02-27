def return_nth_smallest_ascii(s):
    filtered_chars = sorted([c for i, c in enumerate(s) if 48 <= i <= 76])
    return filtered_chars[4] if len(filtered_chars) >= 5 else None