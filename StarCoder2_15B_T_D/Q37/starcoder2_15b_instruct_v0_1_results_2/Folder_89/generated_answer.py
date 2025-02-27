def filter_chars(text: str) -> str:
    filtered_chars = [char for char in text if char < '!' or char > '@' or text.index(char) < 11 or (text.index(char) > 32)]
    return ''.join(filtered_chars)