def return_nth_smallest_ascii(s):
    filtered_chars = [c for i, c in enumerate(s) if 62 <= i <= 83]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[8] if len(sorted_chars) > 8 else None