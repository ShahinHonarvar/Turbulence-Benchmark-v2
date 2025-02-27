def filter_chars(s):
    result = []
    for char in s:
        if not (69 < ord(char) < 97 and 'V' < char < 'j'):
            result.append(char)
    return ''.join(result)