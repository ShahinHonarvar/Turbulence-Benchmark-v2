def insert_after_character(s):
    return ''.join((c + ('q' if c == 'U' else '') for c in s))