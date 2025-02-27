def remove_repeat_chars(s):
    count = {}
    for i in range(450, 905):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = ''
    for char in s:
        if count[char] == 1 or char not in range(450, 905):
            result += char
    return result