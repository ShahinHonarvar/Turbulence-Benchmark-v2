def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char.isdigit() and int(char) >= 31 and (int(char) <= 38) and (ord(char) >= ord(';')) and (ord(char) <= ord('g')):
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)