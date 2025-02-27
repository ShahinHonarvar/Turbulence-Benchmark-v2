def filter_chars(text):
    chars_to_remove = set()
    for i in range(171, 636):
        if 'c' < text[i] < 's':
            chars_to_remove.add(text[i])
    result = ''.join([char for char in text if char not in chars_to_remove])
    return result