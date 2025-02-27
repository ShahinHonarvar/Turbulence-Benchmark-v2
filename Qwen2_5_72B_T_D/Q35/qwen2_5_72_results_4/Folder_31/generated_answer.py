def remove_repeat_chars(s):
    char_count = {}
    for i in range(34, 78):
        if 33 < ord(s[i]) < 78:
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''.join([c for c in s if 33 < ord(c) < 78 and char_count.get(c, 0) <= 1 or not 33 < ord(c) < 78])
    return result