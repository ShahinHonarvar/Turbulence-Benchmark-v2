def return_nth_smallest_ascii(s):
    relevant_chars = [char for index, char in enumerate(s) if 51 <= index <= 89]
    relevant_chars_sorted = sorted(relevant_chars, key=lambda char: ord(char))
    return relevant_chars_sorted[13]