def filter_chars(s):
    chars_to_remove = {chr(code) for code in range(ord('-'), ord('X') + 1)}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) < 46 or s.index(char) > 85))