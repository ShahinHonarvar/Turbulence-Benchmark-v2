def filter_chars(input_string: str) -> str:
    return ''.join([char for i, char in enumerate(input_string) if i < 52 or i >= 88 or (not '&' < char < 'c')])