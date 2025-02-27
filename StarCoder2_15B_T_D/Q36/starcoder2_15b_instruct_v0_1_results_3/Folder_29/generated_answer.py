def filter_chars(text):
    filtered_text = ''
    for char in text:
        if char > 'H' and char < 's':
            continue
        filtered_text += char
    return filtered_text