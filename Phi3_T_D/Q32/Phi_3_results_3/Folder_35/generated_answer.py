def insert_after_character(s):
    return ''.join(['M' + char if char == '9' else char for char in s])