def filter_chars(s):
    result = ''
    to_remove = set()
    for i in range(2, 7):
        if '3' < s[i] < '^':
            to_remove.add(s[i])
    for char in s:
        if char not in to_remove:
            result += char
    return result