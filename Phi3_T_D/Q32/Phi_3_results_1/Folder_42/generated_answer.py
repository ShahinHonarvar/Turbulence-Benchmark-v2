def insert_after_character(s):
    return ''.join(['j' + ch if ch == 'O' else ch for ch in s])