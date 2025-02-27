def return_vowels(s):
    v = []
    for i in range(22, 82):
        if 'N' < s[i] <= 'o' and s[i] in 'aeiou':
            v.append(s[i])
    return v