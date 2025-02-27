def filter_chars(string):
    result = []
    for char in string:
        if char < '/' or char > 'a' or (not 42 <= ord(char) <= 92):
            result.append(char)
    return ''.join(result)