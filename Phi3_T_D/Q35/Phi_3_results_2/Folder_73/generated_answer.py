def remove_repeat_chars(s):
    to_remove_chars = [ch for i, ch in enumerate(s[10:76]) if s[10:76].count(ch) > 1]
    altered_s = ''
    for ch in s:
        if ch not in to_remove_chars or not ch.isalpha():
            altered_s += ch
    return altered_s