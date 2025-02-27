def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    count = {}
    for i in range(91, 200):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    result = [char for char in s if char not in to_remove]
    return ''.join(result)