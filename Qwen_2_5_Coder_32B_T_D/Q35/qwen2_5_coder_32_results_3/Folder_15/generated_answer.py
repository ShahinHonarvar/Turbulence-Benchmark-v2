def remove_repeat_chars(s):
    count = {}
    for i in range(1, 5):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = [char for char in s if count.get(char, 0) == 1 or i not in range(1, 5)]
    return ''.join(result)