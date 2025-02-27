def return_nth_smallest_ascii(s):
    relevant_chars = [s[i] for i in range(46, 83) if i < len(s)]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[15] if len(sorted_chars) > 15 else None