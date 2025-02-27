def insert_after_character(s):
    return ''.join((c + ('T' if c == 'U' else '') for c in s))