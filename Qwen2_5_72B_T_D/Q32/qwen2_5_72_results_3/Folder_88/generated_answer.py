def insert_after_character(s):
    return ''.join([ch + 't' if ch == 'a' else ch for ch in s])