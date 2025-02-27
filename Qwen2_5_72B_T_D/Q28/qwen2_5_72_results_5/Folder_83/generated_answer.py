def return_nth_smallest_ascii(s):
    if 30 < len(s) > 70:
        relevant_chars = s[30:71]
        sorted_chars = sorted(relevant_chars)
        if len(sorted_chars) >= 15:
            return sorted_chars[14]
    return None