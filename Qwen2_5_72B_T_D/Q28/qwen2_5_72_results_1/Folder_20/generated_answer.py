def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[25:65] if c in s]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[5] if len(sorted_chars) > 5 else None