def insert_after_character(s):
    return ''.join((c + '9' if c == '6' else c for c in s))