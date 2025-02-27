def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 18 or i >= 64 or (not (ord(char) > ord('3') and ord(char) < ord('B')))]
    return ''.join(filtered_chars)