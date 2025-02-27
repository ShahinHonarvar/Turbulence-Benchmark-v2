def filter_chars(string):
    filtered_chars = []
    for char in string:
        if 33 <= ord(char) <= 70 and (ord(char) >= ord('7') and ord(char) <= ord('k')):
            continue
        else:
            filtered_chars.append(char)
    return ''.join(filtered_chars)