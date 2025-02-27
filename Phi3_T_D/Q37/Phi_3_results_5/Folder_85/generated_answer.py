def filter_chars(s):
    filtered = [char for char in s if not 28 <= s.index(char) <= 65 or not 'O' <= char <= 'd']
    return ''.join(filtered)