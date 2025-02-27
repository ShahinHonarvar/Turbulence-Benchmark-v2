def filter_chars(s):
    to_remove = set()
    for i in range(55, 66):
        if 'f' < s[i] < '|':
            to_remove.add(s[i])
    result = [char for char in s if char not in to_remove]
    return ''.join(result)