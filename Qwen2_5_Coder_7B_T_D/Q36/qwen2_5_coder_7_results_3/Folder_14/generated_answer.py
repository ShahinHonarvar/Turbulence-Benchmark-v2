def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('Z') + 1, ord('c'))]
    for char in target_chars:
        s = s.replace(char, '')
    return s[41:56]