def filter_chars(s):
    result = []
    for char in s:
        if not 90 < ord(char) < 97 or not 'j' < char < 'w':
            result.append(char)
    return ''.join(result)