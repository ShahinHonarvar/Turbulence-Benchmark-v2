def remove_repeat_chars(s):
    count = {}
    for i in range(2, 5):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if (char not in count or count[char] == 1) and (char != s[2] and char != s[3] and (char != s[4])):
            result.append(char)
    return ''.join(result)