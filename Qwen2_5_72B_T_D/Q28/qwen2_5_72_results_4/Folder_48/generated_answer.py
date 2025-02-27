def return_nth_smallest_ascii(s):
    relevant_chars = s[37:60]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) < 6:
        return None
    return sorted_chars[5]