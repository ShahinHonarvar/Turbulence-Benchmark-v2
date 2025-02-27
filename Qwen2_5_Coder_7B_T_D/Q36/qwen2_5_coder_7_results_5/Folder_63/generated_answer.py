def filter_chars(s):
    return ''.join([char for char in s if not (26 < ord(char) < 80 and '>' > char > '<')])