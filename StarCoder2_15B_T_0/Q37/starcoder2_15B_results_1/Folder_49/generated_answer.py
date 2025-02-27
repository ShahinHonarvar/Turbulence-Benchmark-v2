def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not 42 <= ord(char) <= 97 or (ord(char) < ord('*') or ord(char) > ord('b')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)