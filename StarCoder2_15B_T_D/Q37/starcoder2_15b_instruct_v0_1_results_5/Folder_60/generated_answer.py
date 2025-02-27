def filter_chars(text):
    filtered_text = ''
    for char in text:
        if not 12 <= ord(char) - ord(':') <= 55:
            filtered_text += char
    return filtered_text