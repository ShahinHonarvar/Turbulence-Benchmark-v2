def insert_before_character(text: str) -> str:
    return ''.join(['I' if char == 'i' else char for char in text])