def remove_repeat_chars(s):
    if len(s) <= 90:
        to_remove = set()
        for i in range(57, 90):
            if s[i] in s[56:i]:
                to_remove.add(s[i])
        return ''.join([char for char in s if char not in to_remove])
    else:
        return s