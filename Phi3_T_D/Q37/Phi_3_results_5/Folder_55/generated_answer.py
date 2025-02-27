def filter_chars(s):
    index_range = set(range(1, 6))
    altered_chars = [char for i, char in enumerate(s, 0) if ord(char) >= ord('$') and ord(char) <= ord(';') and (i not in index_range)]
    return ''.join(altered_chars)