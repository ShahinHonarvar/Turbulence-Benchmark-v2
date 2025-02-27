def remove_repeat_chars(s):
    count = {}
    for i in range(77, 84):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if (char not in count or count[char] == 1) and (char < '8' or char > '9'):
            result.append(char)
    return ''.join(result)