def filter_chars(s):
    output = ''
    for c in s:
        if not (58 < ord(c) < 82 and ord('F') < ord(c) < ord('O')):
            output += c
    return output