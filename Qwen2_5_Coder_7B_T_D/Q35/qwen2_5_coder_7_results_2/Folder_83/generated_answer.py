def remove_repeat_chars(s):
    seen = set()
    repeat = set()
    for i, char in enumerate(s):
        if 100 < i < 200:
            if char in seen:
                repeat.add(char)
            else:
                seen.add(char)
    result = [char for char in s if char not in repeat]
    return ''.join(result)