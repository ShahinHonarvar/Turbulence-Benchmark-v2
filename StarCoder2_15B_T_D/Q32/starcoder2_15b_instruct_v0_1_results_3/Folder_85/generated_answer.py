def insert_after_character(string):
    chars = list(string)
    for i, char in enumerate(chars):
        if char == 'o':
            chars.insert(i + 1, 'a')
    return ''.join(chars)