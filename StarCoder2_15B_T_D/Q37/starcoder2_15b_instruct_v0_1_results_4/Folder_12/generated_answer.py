def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if 19 <= i <= 90 and ord('F') <= ord(char) <= ord('h')]
    return ''.join(filtered_chars)