def insert_after_character(text):
    return ''.join([c if c != 'E' else 'Ef' for c in text])