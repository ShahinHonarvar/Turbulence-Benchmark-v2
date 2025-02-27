def insert_after_character(s):
    return ''.join((c + 'u' if c == 't' else c for c in s))