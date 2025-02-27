def filter_chars(s):
    chars_to_remove = set('STUVWXYZ')
    return ''.join([char for char in s if (char < 'S' or char > '}') or not 19 <= s.index(char) <= 33])