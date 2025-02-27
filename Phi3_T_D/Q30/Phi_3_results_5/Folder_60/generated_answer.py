def insert_before_character(text):
    result = ''.join(['P' + char if char == 'C' else char for char in text])
    return result