def insert_after_character(s):
    result = ''.join(['6' + c if c == 'X' else c for c in s])
    return result