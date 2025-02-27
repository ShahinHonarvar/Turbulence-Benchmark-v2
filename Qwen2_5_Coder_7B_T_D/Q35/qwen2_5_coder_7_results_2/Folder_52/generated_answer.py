def remove_repeat_chars(s):
    indices = list(range(38, 81))
    count = [0] * 256
    for i in indices:
        count[ord(s[i])] += 1
    return ''.join((c for i, c in enumerate(s) if count[ord(c)] == 1 or i not in indices))