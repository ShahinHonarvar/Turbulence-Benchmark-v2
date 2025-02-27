def filter_chars(s):
    to_remove = set()
    for i in range(124, 855):
        if 57 >= ord(s[i]) >= 97 or s[i] in '9876543210':
            to_remove.add(s[i])
    result = ''.join([char for char in s if char not in to_remove])
    return result