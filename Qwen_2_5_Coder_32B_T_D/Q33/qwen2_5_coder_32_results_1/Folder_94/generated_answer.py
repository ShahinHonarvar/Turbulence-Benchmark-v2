def return_vowels(s):
    v = []
    for i in range(40, 94):
        if s[i] in 'aeiouAEIOU' and s[i] > '4' and (s[i] <= 'H'):
            v.append(s[i])
    return v