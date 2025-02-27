def filter_chars(s):
    to_remove = set()
    for i in range(11, 73):
        if 11 <= i <= 72 and 'i' <= s[i] <= 'v':
            to_remove.add(s[i])
    result = ''.join([char for char in s if char not in to_remove])
    return result