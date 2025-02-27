def filter_chars(string):
    filtered = [char for char in string if not (71 <= ord(char) <= 96 and '_' <= char <= 'o')]
    return ''.join(filtered)