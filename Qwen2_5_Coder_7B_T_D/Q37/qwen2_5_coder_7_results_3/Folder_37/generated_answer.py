def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord('O'), ord('^') + 1)])
    result = ''.join((ch for ch in s if s.index(ch) < 17 or s.index(ch) > 63 or ch not in chars_to_remove))
    return result