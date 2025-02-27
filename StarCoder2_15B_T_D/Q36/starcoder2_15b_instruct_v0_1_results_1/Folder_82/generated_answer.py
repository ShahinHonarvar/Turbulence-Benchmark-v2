def filter_chars(text):
    filtered_chars = []
    for char in text:
        if char < 'V' or char > 'j' or (ord(char) < 69 or ord(char) >= 97):
            filtered_chars.append(char)
    return ''.join(filtered_chars)