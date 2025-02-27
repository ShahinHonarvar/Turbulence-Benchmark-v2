def insert_before_character(s):
    return ''.join((f'N{ch}' if ch == 'B' else ch for ch in s))