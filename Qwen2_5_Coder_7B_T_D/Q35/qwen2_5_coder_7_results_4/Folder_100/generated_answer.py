def remove_repeat_chars(s):
    count = {}
    for i in range(44, 78):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    chars_to_remove = [char for char, freq in count.items() if freq > 1]
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)