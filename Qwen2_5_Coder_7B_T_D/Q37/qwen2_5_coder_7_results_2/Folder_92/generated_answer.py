def filter_chars(s):
    filtered_chars = [char for char in s if not (4 <= s.find(char) <= 4 and '7' <= char <= 'o')]
    return ''.join(filtered_chars)