def filter_chars(string):
    filtered_chars = [char for char in string if char < 'L' or char > 'a' or 1 <= string.index(char) <= 7]
    return ''.join(filtered_chars)