def filter_chars(s):
    start, end = (43, 80)
    filtered_chars = []
    for i, char in enumerate(s):
        if start <= i <= end and '=' <= char <= 'E':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)