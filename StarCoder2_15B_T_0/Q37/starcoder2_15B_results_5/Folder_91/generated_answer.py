def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'B' or char > 'H' or (char < 'B' and char > 'H'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)