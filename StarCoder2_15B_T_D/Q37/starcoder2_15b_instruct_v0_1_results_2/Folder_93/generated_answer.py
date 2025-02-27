def filter_chars(text):
    filtered_chars = []
    for char in text:
        if char < 'H' or char > 'e' or (char < 'H' and char > 'e'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)