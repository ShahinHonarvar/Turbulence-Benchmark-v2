def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('d'), ord('s'))]
    for char in target_chars:
        s = s.replace(char, '')
    return s