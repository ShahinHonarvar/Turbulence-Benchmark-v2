def insert_before_character(s):
    return ''.join(['e' + char if char == 'E' else char for char in s])