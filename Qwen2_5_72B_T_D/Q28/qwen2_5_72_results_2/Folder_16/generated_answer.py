def return_nth_smallest_ascii(s):
    relevant_chars = s[18:46]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) < 7:
        return None
    return sorted_chars[6]