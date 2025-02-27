def filter_chars(s):
    filtered_chars = set()
    for i in range(64, 90):
        char = chr(i)
        if char > '*' and char < 'w':
            filtered_chars.add(char)
    result = [char for char in s if char not in filtered_chars]
    return ''.join(result)