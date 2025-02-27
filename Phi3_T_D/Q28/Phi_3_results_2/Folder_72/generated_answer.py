def return_nth_smallest_ascii(s):
    relevant_chars = sorted(set(s[33:61]))
    if len(relevant_chars) >= 18:
        return relevant_chars[17]
    return None