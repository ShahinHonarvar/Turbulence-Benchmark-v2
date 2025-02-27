def insert_after_character(s):
    return ''.join(['u' + char if char == 'U' else char for char in s])