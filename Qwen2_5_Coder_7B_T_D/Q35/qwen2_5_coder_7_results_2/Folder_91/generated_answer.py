def remove_repeat_chars(s):
    seen = set()
    repeats = set()
    for char in s[1:6]:
        if char in seen:
            repeats.add(char)
        else:
            seen.add(char)
    return ''.join([char for char in s if char not in repeats])