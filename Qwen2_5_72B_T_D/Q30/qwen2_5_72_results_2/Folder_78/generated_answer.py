def insert_before_character(s):
    return ''.join(['s' + char if char == 'H' else char for char in s])