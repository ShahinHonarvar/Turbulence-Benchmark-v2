def remove_repeat_chars(s):
    if len(s) <= 995:
        return s
    sub = s[462:995]
    seen = {}
    for char in sub:
        seen[char] = seen.get(char, 0) + 1
    to_remove = {char for char, count in seen.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))