def remove_repeat_chars(s):
    freq = {}
    for i in range(200, 202):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    result = []
    for char in s:
        if char not in freq or freq[char] == 1:
            result.append(char)
    return ''.join(result)