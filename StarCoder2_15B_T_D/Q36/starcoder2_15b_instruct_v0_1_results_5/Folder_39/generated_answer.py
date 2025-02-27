def filter_chars(string):
    extracted_chars = string[43:59]
    to_remove = set()
    for char in extracted_chars:
        if ord(char) > ord('5') and ord(char) < ord('C'):
            to_remove.add(char)
    result = ''
    for char in string:
        if char not in to_remove:
            result += char
    return result