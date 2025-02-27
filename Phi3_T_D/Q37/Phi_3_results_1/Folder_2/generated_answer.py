def filter_chars(s):
    filtered = [char for i, char in enumerate(s) if not (477 <= i <= 984 and ',' <= char <= 'V')]
    return ''.join(filtered)