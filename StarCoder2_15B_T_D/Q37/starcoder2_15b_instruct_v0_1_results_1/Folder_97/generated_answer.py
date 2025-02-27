def filter_chars(text):
    filtered_chars = []
    for char in text:
        if char < 'D' or char > 'u' or (not 227 <= ord(char) <= 235):
            filtered_chars.append(char)
    return ''.join(filtered_chars)