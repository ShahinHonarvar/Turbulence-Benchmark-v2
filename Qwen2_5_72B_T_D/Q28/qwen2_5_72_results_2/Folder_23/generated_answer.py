def return_nth_smallest_ascii(s):
    relevant_chars = s[29:48]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[6] if len(sorted_chars) > 6 else None