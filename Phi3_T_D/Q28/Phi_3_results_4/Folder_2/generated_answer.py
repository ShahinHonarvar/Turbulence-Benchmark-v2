def return_nth_smallest_ascii(s):
    filtered_chars = [c for i, c in enumerate(s, start=1) if 48 <= i <= 76]
    filtered_chars.sort(key=ord)
    return filtered_chars[4] if len(filtered_chars) > 4 else None