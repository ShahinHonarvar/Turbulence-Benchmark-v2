def insert_before_character(s):
    return ''.join(['P' + c if c == ' ' else c for c in s])