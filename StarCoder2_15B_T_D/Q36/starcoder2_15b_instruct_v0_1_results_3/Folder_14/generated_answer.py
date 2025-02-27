def filter_chars(text: str) -> str:
    """
    Filters characters in a given string based on their ASCII values.
    """
    filtered_chars = [char for char in text if ord(char) < ord('Z') or ord(char) > ord('c')]
    return ''.join(filtered_chars)