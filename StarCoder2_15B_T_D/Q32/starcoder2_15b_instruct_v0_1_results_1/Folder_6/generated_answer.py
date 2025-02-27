def insert_after_character(s):
    result = ''
    for i in range(len(s)):
        result += s[i]
        if s[i] == 'X':
            result += 'u'
    return result