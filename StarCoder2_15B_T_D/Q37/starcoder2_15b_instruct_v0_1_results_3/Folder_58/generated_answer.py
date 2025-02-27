def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 503 or i > 753 or (not (ord(char) >= ord('9') and ord(char) <= ord('w')))]
    return ''.join(filtered_chars)