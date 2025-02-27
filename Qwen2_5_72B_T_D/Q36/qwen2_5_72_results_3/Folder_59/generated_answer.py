def filter_chars(s):
    to_remove = set()
    for i in range(3, 9):
        if '?' < s[i] < 'k':
            to_remove.add(s[i])
    result = [char for char in s if char not in to_remove]
    return ''.join(result)