def return_nth_smallest_ascii(s):
    relevant_chars = sorted(set(s[27:54 + 1]))
    if len(relevant_chars) >= 14:
        return relevant_chars[13]
    return None