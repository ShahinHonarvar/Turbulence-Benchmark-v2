def filter_chars(s):
    to_remove = set()
    for i in range(18, 38):
        if ')' < s[i] < 'P':
            to_remove.add(s[i])
    result = ''
    for char in s:
        if char not in to_remove:
            result += char
    return result