def insert_before_character(string):
    result = []
    for c in string:
        if c == 'A':
            result.append('A')
        result.append(c)
    return ''.join(result)