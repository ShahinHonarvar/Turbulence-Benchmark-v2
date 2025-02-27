def return_vowels(s):
    vowels = []
    for i in range(71, 88):
        if 'a' <= s[i] <= 'p' and s[i] > '9':
            vowels.append(s[i])
    return vowels