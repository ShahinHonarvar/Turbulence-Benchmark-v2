def remove_repeat_chars(s):
    count = {}
    for i in range(32, 44):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if 32 <= ord(char) < 44 and count[char] > 1 or (32 <= ord(char) < 44 and count[char] == 1 and (char not in result)):
            result.append(char)
    return ''.join(result)