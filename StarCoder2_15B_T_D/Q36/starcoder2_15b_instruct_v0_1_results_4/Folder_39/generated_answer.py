def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if i >= 43 and i < 59 and (not (ord(c) > ord('5') and ord(c) < ord('C'))):
            result += c
    return result