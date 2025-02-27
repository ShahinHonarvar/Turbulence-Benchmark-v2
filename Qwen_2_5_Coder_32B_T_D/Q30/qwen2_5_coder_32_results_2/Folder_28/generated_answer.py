def insert_before_character(s):
    return ''.join(['1' + char if char == 'r' else char for char in s])