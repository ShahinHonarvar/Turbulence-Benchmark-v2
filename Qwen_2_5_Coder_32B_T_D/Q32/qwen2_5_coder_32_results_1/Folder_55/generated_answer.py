def insert_after_character(s):
    return ''.join((c + 'U' if c == 'u' else c for c in s))