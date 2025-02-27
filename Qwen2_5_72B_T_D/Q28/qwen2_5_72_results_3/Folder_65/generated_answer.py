def return_nth_smallest_ascii(s):
    relevant_chars = [c for c in s[32:68] if ord(c) >= 32 and ord(c) <= 126]
    relevant_chars.sort(key=ord)
    return relevant_chars[11] if len(relevant_chars) > 11 else None