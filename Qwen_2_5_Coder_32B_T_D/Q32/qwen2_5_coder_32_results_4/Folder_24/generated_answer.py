def insert_after_character(s):
    return ''.join((c + '4' if c == '0' else c for c in s))