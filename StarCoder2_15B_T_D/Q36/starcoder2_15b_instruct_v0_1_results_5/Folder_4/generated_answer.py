def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 42 or i >= 67 or (not (ord(char) > ord('6') and ord(char) < ord('g')))]
    return ''.join(filtered_chars)