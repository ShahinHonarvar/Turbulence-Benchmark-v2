def insert_after_character(s):
    return ''.join(('w' + char if char == 'r' else char for char in s))