def remove_repeat_chars(s):
    count = {}
    for i in range(25, 80):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    remove = [char for char, cnt in count.items() if cnt > 1]
    result = ''.join([char for char in s if char not in remove])
    return result