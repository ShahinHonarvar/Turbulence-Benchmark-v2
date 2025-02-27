def remove_repeat_chars(s):
    altered_chars = []
    tracked_chars = set()
    for i, char in enumerate(s[49:75]):
        if char not in tracked_chars:
            if s.count(char, 0, 76) > 1:
                s = s.replace(char, '')
            else:
                altered_chars.append(char)
                tracked_chars.add(char)
    return ''.join(altered_chars)