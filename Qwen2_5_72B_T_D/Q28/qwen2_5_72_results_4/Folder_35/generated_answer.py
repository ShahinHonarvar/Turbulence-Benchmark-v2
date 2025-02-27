def return_nth_smallest_ascii(s):
    relevant_chars = [s[i] for i in range(50, 76) if i < len(s)]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[6]