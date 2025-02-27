def return_nth_smallest_ascii(s):
    relevant_chars = [s[i] for i in range(52, 80) if i < len(s)]
    relevant_chars_sorted = sorted(relevant_chars)
    if len(relevant_chars_sorted) < 7:
        return None
    return relevant_chars_sorted[6]