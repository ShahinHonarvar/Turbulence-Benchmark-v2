def filter_chars(s: str) -> str:
    """
    Filters out characters between indices 43 and 83 (both exclusive) in the given string `s`
    if the character is greater than ':' and smaller than 'Q'.
    """
    filtered_chars = [c for i, c in enumerate(s) if i < 43 or i >= 83 or (ord(c) < ord(':') or ord(c) >= ord('Q'))]
    return ''.join(filtered_chars)