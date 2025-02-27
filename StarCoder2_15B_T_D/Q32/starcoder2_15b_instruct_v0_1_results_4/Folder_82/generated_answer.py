def insert_after_character(text: str) -> str:
    """
    Inserts character 'I' immediately succeeding any occurrences of character 'I'
    in the given text.
    """
    return ''.join([c + 'I' if c == 'I' else c for c in text])