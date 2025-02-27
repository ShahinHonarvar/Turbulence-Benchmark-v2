def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[10:83] if char not in s[:10] + s[83:]]
    filtered_chars.sort(key=ord)
    return filtered_chars[17] if len(filtered_chars) >= 18 else None