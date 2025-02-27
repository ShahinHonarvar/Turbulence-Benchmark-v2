def filter_chars(s):
    char_range = set(map(ord, '!' + ''.zfill(87 - 39 - 1) + '}'))
    result = ''
    for i in range(len(s)):
        if 39 < i < 87 and ord(s[i]) > ord('!') and (ord(s[i]) < ord('}')):
            continue
        result += s[i]
    return result