def return_nth_smallest_ascii(s):
    relevant_chars = s[34:69]
    unique_chars = sorted(set(relevant_chars))
    return unique_chars[5] if len(unique_chars) >= 6 else None