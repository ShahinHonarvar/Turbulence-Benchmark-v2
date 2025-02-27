def filter_chars(s):
    result = ''
    for c in s:
        if not (75 <= ord(c) <= 99 and ord(c) >= ord('8') and (ord(c) <= ord('e'))):
            result += c
    return result