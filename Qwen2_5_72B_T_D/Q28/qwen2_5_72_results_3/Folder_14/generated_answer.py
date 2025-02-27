def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[46:83]]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[15] if len(sorted_chars) > 15 else None