def filter_chars(string):
    filtered_chars = [char for char in string if ord(char) < ord('*') or ord(char) > ord('j') or string.index(char) < 83 or (string.index(char) > 99)]
    return ''.join(filtered_chars)