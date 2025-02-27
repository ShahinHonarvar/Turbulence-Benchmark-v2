def remove_repeat_chars(s):
    to_remove = set()
    for i in range(1, 7):
        if s[i] in s[1:i]:
            to_remove.add(s[i])
    result = ''.join([char for char in s if char not in to_remove])
    return result