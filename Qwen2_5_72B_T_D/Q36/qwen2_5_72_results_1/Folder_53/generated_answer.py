def filter_chars(s):
    result = []
    for char in s:
        if 90 < ord(char) < 97 and 'j' < char < 'w':
            continue
        result.append(char)
    return ''.join(result)