def filter_chars(s):
    altered_chars = {char for i, char in enumerate(s[42:67], start=42) if '7' <= char <= 'g'}
    altered_string = ''.join((char for char in s if char not in altered_chars))
    return altered_string