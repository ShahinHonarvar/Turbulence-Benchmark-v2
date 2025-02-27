def return_nth_smallest_ascii(s):
    specific_chars = sorted(set(s[50:90]))
    if len(specific_chars) >= 14:
        return specific_chars[13]
    else:
        return None