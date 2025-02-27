def return_nth_smallest_ascii(s):
    relevant_chars = [char for char in s[47:81]]
    relevant_chars_sorted = sorted(relevant_chars, key=ord)
    return relevant_chars_sorted[3]