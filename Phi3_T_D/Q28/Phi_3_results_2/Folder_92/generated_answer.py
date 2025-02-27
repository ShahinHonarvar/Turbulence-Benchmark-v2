def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[:4])
    return relevant_chars[3]