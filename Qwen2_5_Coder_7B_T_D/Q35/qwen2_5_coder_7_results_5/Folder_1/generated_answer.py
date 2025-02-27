def remove_repeat_chars(s):
    count = {}
    for i in range(17, 88):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = ''
    for char in s:
        if (char not in count or count[char] == 1) and (s.index(char) < 17 or s.rindex(char) > 88):
            result += char
    return result