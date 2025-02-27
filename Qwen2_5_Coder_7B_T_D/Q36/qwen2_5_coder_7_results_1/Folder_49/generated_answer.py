def filter_chars(s):
    filtered_chars = [char for char in s if not (46 < ord(char) < 91 and 'D' < char < 'H')]
    return ''.join(filtered_chars)