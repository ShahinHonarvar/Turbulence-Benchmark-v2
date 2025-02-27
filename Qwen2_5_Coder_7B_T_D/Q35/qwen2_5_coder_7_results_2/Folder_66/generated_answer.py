def remove_repeat_chars(s):
    count = {}
    for i in range(11, 76):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    remove_chars = [char for char, freq in count.items() if freq > 1]
    result = []
    for char in s:
        if char not in remove_chars:
            result.append(char)
    return ''.join(result)