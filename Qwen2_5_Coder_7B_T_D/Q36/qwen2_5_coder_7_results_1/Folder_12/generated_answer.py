def filter_chars(s):
    filtered_chars = [char for char in s if not (32 < ord(char) < 84 and 'm' < char < 'w')]
    return ''.join(filtered_chars)