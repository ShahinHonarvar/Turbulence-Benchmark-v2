def remove_repeat_chars(s):
    seen = {}
    new_s = []
    for i, char in enumerate(s):
        if 37 <= i <= 42:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        else:
            new_s.append(char)
    for char in seen:
        if seen[char] > 1:
            s = s.replace(char, '')
    return ''.join(new_s)