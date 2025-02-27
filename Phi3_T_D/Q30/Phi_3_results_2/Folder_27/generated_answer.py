def insert_before_character(text):
    result = ''.join(['j' + char if char == 'N' else char for char in text])
    return result