def return_nth_smallest_ascii(s):
    selected_chars = s[10:91]
    return min(selected_chars, key=lambda char: ord(char))