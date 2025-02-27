def return_nth_smallest_ascii(s):
    relevant_chars = s[40:61]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[18] if len(sorted_chars) > 18 else None