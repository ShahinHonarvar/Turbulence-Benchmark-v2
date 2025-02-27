def return_vowels(s):
    v = ['a', 'e', 'i', 'o', 'u']
    r = []
    for i in range(max(202, len(s) - 1), min(872, len(s))):
        if '4' < s[i] <= '>' and s[i] in v:
            r.append(s[i])
    return r