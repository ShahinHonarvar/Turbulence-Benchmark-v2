def insert_after_character(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] == 'o':
            result.append('oa')
        else:
            result.append(s[i])
        i += 1
    return ''.join(result)