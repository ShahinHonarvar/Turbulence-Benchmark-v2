def remove_repeat_chars(s):
    if len(s) <= 9:
        return ''
    seen, duplicates = ({}, set())
    for i in range(1, 8):
        char = s[i]
        if char in seen:
            seen[char] += 1
            duplicates.add(char)
        else:
            seen[char] = 1
    return ''.join([c for c in s if c not in duplicates])