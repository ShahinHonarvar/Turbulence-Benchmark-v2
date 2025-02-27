def insert_before_character(s):
    return ''.join(['U' + char if char == 'U' else char for char in s])