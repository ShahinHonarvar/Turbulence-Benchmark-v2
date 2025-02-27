def filter_chars(text):
    result = [''] * len(text)
    j = 0
    for i, c in enumerate(text):
        if i >= 18 and i < 64 and (ord(c) > ord('3')) and (ord(c) < ord('B')):
            continue
        result[j] = c
        j += 1
    return ''.join(result)