def filter_chars(s):
    return ''.join([char for char in s if not 155 <= s.index(char) <= 403 or '(' > char > ']'])