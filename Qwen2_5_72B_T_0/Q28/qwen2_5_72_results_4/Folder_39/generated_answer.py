def return_nth_smallest_ascii(s):
    if len(s) < 2 or len(s) > 67:
        return None
    relevant_chars = s[1:67]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[7] if len(sorted_chars) > 7 else None