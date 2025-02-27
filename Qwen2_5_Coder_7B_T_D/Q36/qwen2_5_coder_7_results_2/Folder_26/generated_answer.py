def filter_chars(s):
    to_remove = [chr(i) for i in range(ord(':') + 1, ord('Q'))]
    for char in to_remove:
        s = s.replace(char, '')
    return s