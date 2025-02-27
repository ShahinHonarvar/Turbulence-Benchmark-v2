def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[13:36])
    return relevant_chars[17] if len(relevant_chars) >= 18 else None