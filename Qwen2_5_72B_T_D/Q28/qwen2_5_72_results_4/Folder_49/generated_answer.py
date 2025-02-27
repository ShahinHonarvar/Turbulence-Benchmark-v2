def return_nth_smallest_ascii(s):
    if len(s) < 81:
        return None
    relevant_chars = s[20:81]
    sorted_chars = sorted(set(relevant_chars))
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]