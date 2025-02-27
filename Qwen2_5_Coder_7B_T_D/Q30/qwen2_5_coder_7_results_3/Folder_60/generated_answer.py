def insert_before_character(s):
    return ''.join(('PC' if char == 'C' else char for char in s))