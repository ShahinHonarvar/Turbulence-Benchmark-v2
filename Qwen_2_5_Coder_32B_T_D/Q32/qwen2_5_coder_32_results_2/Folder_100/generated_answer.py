def insert_after_character(s):
    return ''.join((f'{char} ' if char == '0' else char for char in s))