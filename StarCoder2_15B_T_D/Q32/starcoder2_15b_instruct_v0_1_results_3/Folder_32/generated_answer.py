def insert_after_character(string):
    return ''.join([c if c != 'F' else 'uF' for c in string])