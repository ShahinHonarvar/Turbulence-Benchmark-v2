def insert_after_character(s):
    return ''.join((c + ('n' if c == 'a' else '') for c in s))