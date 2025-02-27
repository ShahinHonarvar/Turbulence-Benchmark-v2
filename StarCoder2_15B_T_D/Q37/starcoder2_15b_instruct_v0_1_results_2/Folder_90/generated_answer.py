def filter_chars(string):
    result = ''
    for char in string:
        if char < 'J' or char > 'b' or 348 <= ord(char) <= 852:
            result += char
    return result