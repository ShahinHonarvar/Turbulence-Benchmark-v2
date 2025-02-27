def filter_chars(s):
    removal_chars = set()
    for i in range(344, 874):
        if 'f' < s[i] < '~':
            removal_chars.add(s[i])
    result = ''.join([char for char in s if char not in removal_chars])
    return result