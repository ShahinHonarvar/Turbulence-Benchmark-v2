def remove_repeat_chars(s):
    skip_chars = set()
    for i in range(80, 200):
        if s[i] in skip_chars:
            continue
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                skip_chars.add(s[i])
                break
    return ''.join([char for char in s if char not in skip_chars])