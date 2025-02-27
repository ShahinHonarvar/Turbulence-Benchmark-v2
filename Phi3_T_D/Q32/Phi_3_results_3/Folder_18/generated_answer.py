def insert_after_character(s):
    return ''.join(['l' + char if char == 'K' else char for char in s])