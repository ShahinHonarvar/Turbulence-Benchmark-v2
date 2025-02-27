def return_vowels(s):
    vowels = []
    for i in range(20, 43):
        if s[i] in ['a', 'e', 'i', 'o', 'u'] and '5' < s[i] <= 'M':
            vowels.append(s[i])
    return vowels