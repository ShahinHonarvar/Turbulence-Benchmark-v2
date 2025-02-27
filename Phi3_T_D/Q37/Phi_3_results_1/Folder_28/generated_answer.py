def filter_chars(s):
    filtered_str = []
    for i, char in enumerate(s):
        if 20 <= i <= 79 and '!' <= char <= 'T':
            continue
        filtered_str.append(char)
    return ''.join(filtered_str)