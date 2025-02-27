def filter_chars(input_str):
    altered_str = [char for i, char in enumerate(input_str) if not (24 <= i <= 82 and '5' <= char <= '<')]
    return ''.join(altered_str)