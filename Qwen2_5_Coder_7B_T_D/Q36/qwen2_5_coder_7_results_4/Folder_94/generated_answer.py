def filter_chars(s):
    filtered_chars = set()
    for i in range(15, 85):
        if 'I' < s[i] < 'M':
            filtered_chars.add(s[i])
    result = []
    for char in s:
        if char not in filtered_chars:
            result.append(char)
    return ''.join(result)