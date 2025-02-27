def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (155 <= ord(char) <= 403 and ord(char) >= ord('(') and (ord(char) <= ord(']'))):
            filtered_chars.append(char)
    return ''.join(filtered_chars)