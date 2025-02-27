def filter_chars(s):
    result = list(s)
    for i in range(24, 83):
        if '5' <= s[i] <= '<':
            result = [char for char in result if char != s[i]]
    return ''.join(result)