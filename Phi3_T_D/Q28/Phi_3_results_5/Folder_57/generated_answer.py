def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[17:35]))
    if len(unique_chars) >= 18:
        return unique_chars[17]
    return None