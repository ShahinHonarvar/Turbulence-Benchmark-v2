def insert_after_character(s):
    return ''.join((c + 'i' if c == 'I' else c for c in s))