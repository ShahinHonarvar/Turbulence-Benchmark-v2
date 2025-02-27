def return_nth_smallest_ascii(s):
    relevant_chars = s[40:61]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) < 19:
        return None
    return sorted_chars[18]