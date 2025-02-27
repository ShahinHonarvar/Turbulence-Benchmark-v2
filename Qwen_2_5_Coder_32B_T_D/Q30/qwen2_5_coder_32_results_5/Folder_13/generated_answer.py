def insert_before_character(s):
    return ''.join(['N' + char if char == 'x' else char for char in s])