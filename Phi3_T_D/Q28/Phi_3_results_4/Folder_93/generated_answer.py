def return_nth_smallest_ascii(s):
    substr = s[42:60]
    unique_chars = {char for char in substr}
    smallest_char = min(unique_chars, key=ord)
    nth_smallest = sorted(unique_chars, key=ord)[16]
    return nth_smallest