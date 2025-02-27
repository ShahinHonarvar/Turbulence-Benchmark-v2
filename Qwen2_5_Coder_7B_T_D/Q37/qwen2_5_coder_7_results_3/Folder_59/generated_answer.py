def filter_chars(s):
    filtered_chars = [char for char in s if not (2 <= s.index(char) <= 3 and '5' <= char <= '_')]
    return ''.join(filtered_chars)