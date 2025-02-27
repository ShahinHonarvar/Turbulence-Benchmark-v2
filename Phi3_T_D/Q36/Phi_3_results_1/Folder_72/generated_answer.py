def filter_chars(s):
    modified_chars = [char for char in s[:44] + s[68:] if not 44 < ord(char) < ord('x')]
    return ''.join(modified_chars)