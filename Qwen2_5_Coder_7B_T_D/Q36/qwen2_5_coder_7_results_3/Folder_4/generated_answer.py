def filter_chars(s):
    filtered_chars = set()
    for i in range(42, 67):
        char = s[i]
        if '6' < char < 'g':
            filtered_chars.add(char)
    result = []
    for char in s:
        if char not in filtered_chars:
            result.append(char)
    return ''.join(result)