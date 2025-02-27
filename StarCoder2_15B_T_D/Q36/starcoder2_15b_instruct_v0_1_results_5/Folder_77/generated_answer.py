def filter_chars(string: str) -> str:
    index = 221
    while index < 419 and index < len(string):
        char = string[index]
        if ord(char) > ord('-') and ord(char) < ord('v'):
            string = string.replace(char, '')
        else:
            index += 1
    return string