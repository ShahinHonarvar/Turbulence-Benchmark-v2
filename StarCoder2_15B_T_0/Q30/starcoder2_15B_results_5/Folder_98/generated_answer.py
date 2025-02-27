def insert_before_character(string):
    return string.replace('U', 'uU').replace('uU', 'uUu').replace('uUu', 'uUuu')