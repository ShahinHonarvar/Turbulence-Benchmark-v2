def filter_chars(s):
    to_remove = [chr(i) for i in range(ord('2'), ord('J')) if i > ord('1') and i < ord('J')]
    to_remove = set(to_remove)
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)