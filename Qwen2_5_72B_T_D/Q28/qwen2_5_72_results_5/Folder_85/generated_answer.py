def return_nth_smallest_ascii(s):
    relevant_chars = s[17:87]
    sorted_chars = sorted(relevant_chars, key=ord)
    return sorted_chars[14] if len(sorted_chars) > 14 else None