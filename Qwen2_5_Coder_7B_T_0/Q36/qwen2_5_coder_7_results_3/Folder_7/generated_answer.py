def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('W') + 1, ord('y'))]
    for char in target_chars:
        s = s.replace(char, '')
    return s