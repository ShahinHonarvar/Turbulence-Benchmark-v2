def return_nth_smallest_ascii(s):
    filtered_chars = sorted([s[i] for i in range(25, 78) if s[i] in s])
    return filtered_chars[15] if len(filtered_chars) > 15 else None