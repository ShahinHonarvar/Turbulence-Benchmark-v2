def return_nth_smallest_ascii(s):
    relevant_chars = s[60:84]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[13] if len(sorted_chars) > 13 else None