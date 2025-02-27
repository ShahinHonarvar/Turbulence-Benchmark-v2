def return_nth_smallest_ascii(s):
    relevant_chars = [s[i] for i in range(12, 88) if 0 <= i < len(s)]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[16] if len(sorted_chars) > 16 else None