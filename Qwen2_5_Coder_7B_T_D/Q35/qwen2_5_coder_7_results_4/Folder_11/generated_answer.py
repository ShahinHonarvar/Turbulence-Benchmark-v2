def remove_repeat_chars(s):
    count = {}
    for i in range(48, 76):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if count[char] == 1 or not 48 < ord(char) < 76:
            result.append(char)
    return ''.join(result)