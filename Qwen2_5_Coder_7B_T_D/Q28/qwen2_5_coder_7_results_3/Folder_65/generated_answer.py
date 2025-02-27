def return_nth_smallest_ascii(s):
    filtered_chars = sorted((c for c in s[32:68] if c.isalpha()))
    if len(filtered_chars) >= 12:
        return filtered_chars[11]
    else:
        return None