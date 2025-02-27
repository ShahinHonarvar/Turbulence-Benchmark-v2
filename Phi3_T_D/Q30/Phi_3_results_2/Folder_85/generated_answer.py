def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'o':
            result += 'a' + c
        else:
            result += c
    return result