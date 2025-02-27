def return_nth_smallest_ascii(s):
    target_chars = s[17:84]
    return min(target_chars, key=lambda char: ord(char))