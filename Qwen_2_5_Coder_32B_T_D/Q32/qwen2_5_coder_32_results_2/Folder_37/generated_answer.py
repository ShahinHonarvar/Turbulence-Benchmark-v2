def insert_after_character(s):
    return ''.join(['a' if i == 'U' else i for i in s] + ['a' if s.endswith('U') else ''])