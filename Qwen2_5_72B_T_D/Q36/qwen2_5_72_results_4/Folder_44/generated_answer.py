def filter_chars(s):
    to_remove = set()
    for i in range(18, 64):
        if '3' < s[i] < 'B':
            to_remove.add(s[i])
    result = [char for char in s if char not in to_remove]
    return ''.join(result)