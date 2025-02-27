def insert_after_character(s):
    return ''.join(['a' + char if char == 'A' else char for char in s])