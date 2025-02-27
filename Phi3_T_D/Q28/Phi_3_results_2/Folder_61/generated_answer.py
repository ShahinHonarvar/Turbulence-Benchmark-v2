def return_nth_smallest_ascii(s):
    relevant_chars = s[:10]
    return min(relevant_chars, key=ord)