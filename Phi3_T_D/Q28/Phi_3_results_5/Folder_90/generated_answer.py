def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[17:84])
    return relevant_chars[4] if len(relevant_chars) >= 5 else None