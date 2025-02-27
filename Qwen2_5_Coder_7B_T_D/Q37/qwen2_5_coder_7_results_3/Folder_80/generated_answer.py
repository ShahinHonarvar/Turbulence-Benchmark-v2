def filter_chars(s):
    chars_to_remove = set('abcdefghi')
    result = ''.join((char for char in s if 36 <= s.index(char) <= 79 and char not in chars_to_remove))
    return result