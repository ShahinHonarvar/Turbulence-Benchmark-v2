def return_nth_smallest_ascii(s):
    relevant_chars = s[38:83]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[19]