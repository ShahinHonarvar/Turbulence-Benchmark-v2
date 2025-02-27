def filter_chars(string):
    return ''.join((char for index, char in enumerate(string) if not (124 <= index <= 854 and '9' <= char <= 's')))