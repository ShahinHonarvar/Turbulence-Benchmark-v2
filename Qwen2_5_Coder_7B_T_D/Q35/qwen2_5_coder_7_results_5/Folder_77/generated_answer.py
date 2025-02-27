def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(356, 988):
        count[ord(s[i])] += 1
    result = []
    for i in range(356, 988):
        if count[ord(s[i])] == 1:
            result.append(s[i])
    return ''.join(result) + s[:355] + s[988:]