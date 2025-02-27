def filter_chars(s):
    remove_set = set()
    for i in range(45, 57):
        if 'F' < s[i] < 'n':
            remove_set.add(s[i])
    result = ''.join([c for c in s if c not in remove_set])
    return result