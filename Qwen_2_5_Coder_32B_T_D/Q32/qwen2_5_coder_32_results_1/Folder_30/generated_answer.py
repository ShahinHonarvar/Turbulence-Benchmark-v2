def insert_after_character(s):
    return ''.join(('F' + c if c == '4' else c for c in s))