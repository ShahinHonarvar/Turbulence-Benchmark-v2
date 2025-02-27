def filter_chars(s):
    filter_set = set('PQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    result = []
    for i, char in enumerate(s):
        if 12 <= i <= 25 and char in filter_set:
            result.append(char)
    return ''.join(result)