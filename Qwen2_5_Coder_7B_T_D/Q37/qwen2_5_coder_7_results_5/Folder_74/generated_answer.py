def filter_chars(s):
    chars_to_remove = set('fghijklmno')
    result = ''.join([char for char in s if (char < 'f' or char > 'o') or (19 > i or i > 32) for i, char in enumerate(s)])
    return result