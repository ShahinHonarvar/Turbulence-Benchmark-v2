def insert_before_character(s):
    return ''.join((char if char != 'i' else 'ii' for char in s))