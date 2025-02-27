def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if 83 <= i <= 99 and (ord(c) >= ord('*') and ord(c) <= ord('j')):
            continue
        result += c
    return result