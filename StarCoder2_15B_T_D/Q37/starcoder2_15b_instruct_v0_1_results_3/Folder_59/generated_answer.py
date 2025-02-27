def filter_chars(string: str) -> str:
    return ''.join((char for i, char in enumerate(string) if (i < 2 or i > 3) or (ord(char) < ord('5') or ord(char) > ord('_'))))