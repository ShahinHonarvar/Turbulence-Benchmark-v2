def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[1:32] if c in s]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[5] if len(sorted_chars) > 5 else None