def remove_repeat_chars(s):
    char_count = {}
    for i in range(91, 97):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((c for c in s if c not in repeated_chars))