def insert_after_character(s):
    return ''.join((x + 'S' if x == '2' else x for x in s))