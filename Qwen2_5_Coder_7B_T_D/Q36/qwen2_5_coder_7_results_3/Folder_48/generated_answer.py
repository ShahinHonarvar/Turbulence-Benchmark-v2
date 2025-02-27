def filter_chars(s):
    result = list(s)
    for i in range(154, 222):
        if 'A' < s[i] < 'f':
            result = [char for char in result if char != s[i]]
    return ''.join(result)