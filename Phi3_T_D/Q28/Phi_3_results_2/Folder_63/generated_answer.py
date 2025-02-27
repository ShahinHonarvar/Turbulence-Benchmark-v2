def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[47:71])
    return relevant_chars[13] if len(relevant_chars) >= 14 else None