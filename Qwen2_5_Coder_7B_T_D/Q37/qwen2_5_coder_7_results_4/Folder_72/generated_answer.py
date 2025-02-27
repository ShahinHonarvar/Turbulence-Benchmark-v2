def filter_chars(s):
    chars_to_remove = set('HJKLMNPQRSTUVWXYZhjklmnpqrstuvwxyz')
    result = ''
    for i in range(len(s)):
        if 35 <= i <= 51 and s[i] in chars_to_remove:
            continue
        result += s[i]
    return result