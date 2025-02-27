def insert_before_character(s):
    result = ''.join(['0' + c if c == 'e' else c for c in s])
    return result