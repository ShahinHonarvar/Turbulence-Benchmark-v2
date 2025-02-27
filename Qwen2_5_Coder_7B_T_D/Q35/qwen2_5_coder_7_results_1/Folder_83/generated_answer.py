def remove_repeat_chars(s):
    seen = set()
    remove = set()
    for i, char in enumerate(s):
        if 100 < i < 200:
            if char in seen:
                remove.add(char)
            else:
                seen.add(char)
    return ''.join((char for char in s if char not in remove))