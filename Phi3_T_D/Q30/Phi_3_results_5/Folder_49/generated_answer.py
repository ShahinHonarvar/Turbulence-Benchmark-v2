def insert_before_character(s, ch='i'):
    return ''.join([c + 'i' if c == ch and i + 1 < len(s) and (s[i + 1] != ch) else c for i, c in enumerate(s)])