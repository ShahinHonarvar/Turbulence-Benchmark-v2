def insert_after_character(s):
    result = ['4' if char == '0' else char for char in s]
    return ''.join(result)