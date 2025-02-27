def insert_before_character(text: str) -> str:
    """
    Inserts character 'N' immediately preceding any occurrences of character 'x'
    in the given text.
    """
    return ''.join([char if char != 'x' else 'Nx' for char in text])