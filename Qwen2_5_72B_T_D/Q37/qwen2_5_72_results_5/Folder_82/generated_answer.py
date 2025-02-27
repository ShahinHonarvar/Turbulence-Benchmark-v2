def filter_chars(s):
    to_remove = set()
    for i in range(12, 26):
        if 12 <= i <= 25 and 'P' <= s[i] <= 'x':
            to_remove.add(s[i])
    result = ''.join([char for char in s if char not in to_remove])
    return result