def insert_after_character(s):
    return ''.join(['R' + char if char == '5' else char for char in s])