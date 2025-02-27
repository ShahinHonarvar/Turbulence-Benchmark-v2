def filter_chars(text):
    filtered_chars = []
    for char in text:
        if char > '*' and char < '[':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)