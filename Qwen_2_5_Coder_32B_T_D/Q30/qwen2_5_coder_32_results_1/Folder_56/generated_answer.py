def insert_before_character(s):
    return ''.join(['i' + char if char == 'I' else char for char in s])