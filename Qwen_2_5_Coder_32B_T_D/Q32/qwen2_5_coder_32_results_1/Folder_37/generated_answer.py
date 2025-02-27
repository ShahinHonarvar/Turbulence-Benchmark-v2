def insert_after_character(s):
    return ''.join((c + 'a' if c == 'U' else c for c in s))