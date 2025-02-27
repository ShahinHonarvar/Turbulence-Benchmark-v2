def filter_chars(s):
    chars_to_remove = ''.join([chr(i) for i in range(ord(':'), ord('L') + 1)])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s