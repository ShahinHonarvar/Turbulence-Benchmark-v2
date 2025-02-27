def filter_chars(s):
    new_s = ''.join([char for char in s if not 171 <= ord(char) < 636 or not 'c' > char > 's'])
    return new_s