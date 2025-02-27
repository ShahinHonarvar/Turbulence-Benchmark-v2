def filter_chars(s):
    c, s = ('c', 's')
    chars_to_remove = {chr(i) for i in range(ord(c) + 1, ord(s))}
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result