def insert_after_character(s):
    return ''.join((c + 'q' if c == 'j' else c for c in s))