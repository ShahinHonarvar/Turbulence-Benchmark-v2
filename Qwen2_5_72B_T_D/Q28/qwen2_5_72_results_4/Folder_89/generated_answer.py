def return_nth_smallest_ascii(s):
    filtered_chars = [s[i] for i in range(24, min(72, len(s))) if s[i] in s[24:72]]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[7] if len(sorted_chars) > 7 else None