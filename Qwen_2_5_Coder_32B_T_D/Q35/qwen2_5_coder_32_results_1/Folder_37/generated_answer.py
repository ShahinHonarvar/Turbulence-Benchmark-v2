def remove_repeat_chars(s):
    to_remove = set()
    for i in range(3, 7):
        if s[i] in s[3:7]:
            to_remove.add(s[i])
    result = [char for char in s if char not in to_remove]
    return ''.join(result)