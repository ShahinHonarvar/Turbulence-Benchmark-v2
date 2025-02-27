def remove_repeat_chars(s):
    count = {}
    for i in range(1, 4):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = ''
    for char in s:
        if (char not in count or count[char] == 1) and char != s[0] and (char != s[4]):
            result += char
    return result