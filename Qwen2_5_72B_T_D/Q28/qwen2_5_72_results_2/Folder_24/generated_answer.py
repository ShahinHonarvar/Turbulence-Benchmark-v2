def return_nth_smallest_ascii(s):
    relevant_chars = s[34:82]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[11] if len(sorted_chars) > 11 else None