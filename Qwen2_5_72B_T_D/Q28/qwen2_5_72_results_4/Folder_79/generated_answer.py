def return_nth_smallest_ascii(s):
    substr = s[13:36]
    sorted_chars = sorted(substr)
    if len(sorted_chars) < 18:
        return None
    return sorted_chars[17]