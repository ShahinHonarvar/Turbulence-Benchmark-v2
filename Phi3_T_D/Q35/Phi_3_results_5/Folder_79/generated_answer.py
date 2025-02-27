def remove_repeat_chars(s):
    odd_occurrence = set()
    even_occurrence = set()
    for i in range(1, 7):
        char = s[i]
        if i % 2 == 0:
            even_occurrence.add(char)
        else:
            odd_occurrence.add(char)
    for char in odd_occurrence & even_occurrence:
        s = s.replace(char, '')
    return s