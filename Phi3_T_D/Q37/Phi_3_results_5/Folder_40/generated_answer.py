def filter_chars(s):
    start, end = (ord('*'), ord('s'))
    filtered_chars = ''.join((char for char in s if ord(char) < start or ord(char) > end))
    return filtered_chars