def insert_before_character(s):
    return ''.join(['a' if i.endswith('e') else i for i in s.split('e')])