def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[46:73])
    return relevant_chars[14] if len(relevant_chars) >= 15 else None