def filter_chars(text: str) -> str:
    char_range = range(309, 591)
    filtered_chars = [char for i, char in enumerate(text) if i not in char_range or char <= 'S' or char >= 'm']
    return ''.join(filtered_chars)