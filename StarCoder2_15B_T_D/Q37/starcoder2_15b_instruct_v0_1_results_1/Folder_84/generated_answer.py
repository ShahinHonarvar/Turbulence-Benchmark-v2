def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (138 <= ord(char) <= 920 and ord(char) >= ord('6') and (ord(char) <= ord('A'))):
            filtered_chars.append(char)
    return ''.join(filtered_chars)