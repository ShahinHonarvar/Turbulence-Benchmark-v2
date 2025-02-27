def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[1:67])
    return relevant_chars[7] if len(relevant_chars) >= 8 else None