def return_nth_smallest_ascii(s):
    relevant_chars = [s[i] for i in range(58, 86) if i < len(s)]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[18] if len(sorted_chars) > 18 else None