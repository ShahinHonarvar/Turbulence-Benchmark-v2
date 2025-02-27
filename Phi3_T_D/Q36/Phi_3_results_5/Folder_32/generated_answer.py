def filter_chars(s):
    output = []
    for i in range(40, 63):
        if '7' < s[i] < 'H':
            output.extend([c for c in s if c != s[i]])
        else:
            output.append(s[i])
    return ''.join(output)