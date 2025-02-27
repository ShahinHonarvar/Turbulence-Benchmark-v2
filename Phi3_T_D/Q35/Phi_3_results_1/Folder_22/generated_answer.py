def remove_repeat_chars(s):
    chars_to_remove = set()
    seen = {c: False for c in s[50:200]}
    for char in s[50:200]:
        if seen[char]:
            chars_to_remove.add(char)
        else:
            seen[char] = True
    altered_s = ''.join((c for c in s if c not in chars_to_remove or not chars_to_remove))[50:200]
    return altered_s