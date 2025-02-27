def return_nth_smallest_ascii(s):
    filtered_chars = [c for i, c in enumerate(s) if 1 <= i <= 31]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[5] if len(sorted_chars) > 5 else None