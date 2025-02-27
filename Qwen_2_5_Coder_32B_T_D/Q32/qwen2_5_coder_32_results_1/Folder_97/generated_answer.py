def insert_after_character(s):
    return ''.join((c + ('h' if c == 'o' else '') for c in s))