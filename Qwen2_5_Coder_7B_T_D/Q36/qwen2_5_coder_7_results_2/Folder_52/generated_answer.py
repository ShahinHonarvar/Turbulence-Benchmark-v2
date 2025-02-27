def filter_chars(s):
    char_range = set('JKLMNOPQRSTUVWXYZ')
    return ''.join([char for char in s if char not in char_range or char < 'I' or char >= 'a'])