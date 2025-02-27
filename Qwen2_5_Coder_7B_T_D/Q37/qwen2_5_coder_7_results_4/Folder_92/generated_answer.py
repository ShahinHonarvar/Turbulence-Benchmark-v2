def filter_chars(s):
    filtered_chars = set()
    for i in range(4, 5):
        if '7' <= s[i] <= 'o':
            filtered_chars.add(s[i])
    result = ''.join([char for char in s if char not in filtered_chars])
    return result