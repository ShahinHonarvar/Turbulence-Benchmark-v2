def remove_repeat_chars(s):
    start, end = (73, 84)
    count = {}
    for i in range(start, end):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    altered = [ch for ch in s if ch < 'a' or not ch.isalpha() or count[ch] == 1 or (ch >= 'z') or (ch not in count)]
    return ''.join(altered)