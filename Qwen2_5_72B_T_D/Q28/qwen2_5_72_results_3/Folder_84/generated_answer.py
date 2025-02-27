def return_nth_smallest_ascii(s):
    if 52 <= len(s) > 79:
        relevant_chars = s[52:80]
        sorted_chars = sorted(relevant_chars)
        return sorted_chars[6]
    return None